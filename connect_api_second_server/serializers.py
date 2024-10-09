from rest_framework import serializers
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from account.models import CustomUser
from advertisement.models import Advertisement
from .models import Provider, Product, Industry
import jwt


class ConnectSerializer(serializers.Serializer):
    id_user = serializers.CharField(
        label=_("id_user"),
        write_only=True
    )
    entry = serializers.CharField(
        label=_("entry"),
        write_only=True
    )

    def validate(self, data):
        id_user = data.get('id_user')
        entry = data.get('entry')

        if id_user and entry:
            return True
        else:
            msg = _('Не хватает данных.')
            raise serializers.ValidationError(msg)


class CreateUnderTableAdvertisementSerializer(serializers.Serializer):
    token = serializers.CharField(label='token')
    adv_id = serializers.CharField(label='adv_id')
    type_services = serializers.CharField(label='type_services')

    title = serializers.CharField(label='title')
    text_in = serializers.CharField(label='text_in')

    skill_level = serializers.CharField(label='skill_level', default=None)
    details = serializers.CharField(label='details', default=None)
    founding_date = serializers.CharField(label='founding_date', default=None)

    def validate(self, attrs):
        token = attrs.get('token')
        type_services = attrs.get('type_services').lower()
        if token:
            try:
                auth = jwt.decode(
                    token, key=settings.SECRET_KEY, algorithms=["HS256"])
            except jwt.exceptions.DecodeError:
                raise serializers.ValidationError(code='authorization')
        else:
            raise serializers.ValidationError(code='authorization')
        if type_services == 'услуга':  # provider
            if attrs.get('skill_level') != None:
                exp_dict = {
                    "adv_id": attrs.get('adv_id'),
                    "title": attrs.get('title'),
                    "text_in": attrs.get('text_in'),
                    "skill_level": attrs.get('skill_level')
                }
            else:
                raise serializers.ValidationError(code='authorization')

            Provider.objects.create(**exp_dict)
            attrs['auth'] = auth
            return attrs

        elif type_services == 'товар':  # product
            if attrs.get('details') != None:
                exp_dict = {
                    "adv_id": attrs.get('adv_id'),
                    "title": attrs.get('title'),
                    "text_in": attrs.get('text_in'),
                    "details": attrs.get('details')
                }
            else:
                raise serializers.ValidationError(code='authorization')

            Product.objects.create(**exp_dict)
            attrs['auth'] = auth
            return attrs
        else:  # industry
            if attrs.get('founding_date') != None:
                exp_dict = {
                    "adv_id": attrs.get('adv_id'),
                    "title": attrs.get('title'),
                    "text_in": attrs.get('text_in'),
                    "founding_date": attrs.get('founding_date')
                }
            else:
                raise serializers.ValidationError(code='authorization')

            Industry.objects.create(**exp_dict)
            attrs['auth'] = auth
            return attrs


class TakeMarketingSpecificSerializer(serializers.Serializer):
    token = serializers.CharField(label='token')
    adv_id = serializers.CharField(label='adv_id')

    def validate(self, attrs):
        token = attrs.get('token')
        adv_id = attrs.get('adv_id')
        if token:
            try:
                auth = jwt.decode(
                    token, key=settings.SECRET_KEY, algorithms=["HS256"])
            except jwt.exceptions.DecodeError:
                raise serializers.ValidationError(code='authorization')
        else:
            raise serializers.ValidationError(code='authorization')

        marketing = Advertisement.objects.get(adv_id=adv_id)
        type_services = marketing.type_services
        exp_dict = {
            "economic_works": f'{marketing.economic_works}',
            "type_services": f'{type_services}',
        }
        if type_services == 'услуга':
            marketing_twotable = Provider.objects.get(adv=adv_id)
            exp_dict.update([('title', f'{marketing_twotable.title}')])
            exp_dict.update([('text_in', f'{marketing_twotable.text_in}')])
            exp_dict.update(
                [('skill_level', f'{marketing_twotable.skill_level}')])
            # exp_dict.update([('text_out', f'{marketing_twotable.text_out}')])
            attrs.update(exp_dict)
            return attrs
        elif type_services == 'товар':
            marketing_twotable = Product.objects.get(adv=adv_id)
            exp_dict.update([('title', f'{marketing_twotable.title}')])
            exp_dict.update([('text_in', f'{marketing_twotable.text_in}')])
            exp_dict.update([('details', f'{marketing_twotable.details}')])
            # exp_dict.update([('text_out', f'{marketing_twotable.text_out}')])
            attrs.update(exp_dict)
            return attrs
        elif type_services == 'предприятие':
            marketing_twotable = Industry.objects.get(adv=adv_id)
            exp_dict.update([('title', f'{marketing_twotable.title}')])
            exp_dict.update([('text_in', f'{marketing_twotable.text_in}')])
            exp_dict.update(
                [('founding_date', f'{marketing_twotable.founding_date}')])
            # exp_dict.update([('text_out', f'{marketing_twotable.text_out}')])
            attrs.update(exp_dict)
            return attrs


class UpdateUnderTableAdvertisementSerializer(serializers.Serializer):
    token = serializers.CharField(label='token')
    adv_id = serializers.CharField(label='adv_id')
    text_out = serializers.CharField(label='text_out')

    def validate(self, attrs):
        token = attrs.get('token')
        adv_id = attrs.get('adv_id')
        if token:
            try:
                auth = jwt.decode(
                    token, key=settings.SECRET_KEY, algorithms=["HS256"])
            except jwt.exceptions.DecodeError:
                raise serializers.ValidationError(code='authorization')
        else:
            raise serializers.ValidationError(code='authorization')
        
        exp_model = [Product,Provider,Industry]
        print(exp_model,type(exp_model))

        for iterator in exp_model:
            #try:
            if iterator.objects.filter(adv_id=adv_id).exists():
                iterator.objects.update(text_out=attrs.get('text_out'))
            else:
                continue
            #except DoesNotExist
                
                    
        return attrs



class TextAdvertisementOutputSerializer(serializers.Serializer):
    token = serializers.CharField(label='token')
    adv_id = serializers.CharField(label='adv_id')
    #text_out = serializers.CharField(label='text_out')

    def validate(self, attrs):
        token = attrs.get('token')
        adv_id = attrs.get('adv_id')
        if token:
            try:
                auth = jwt.decode(
                    token, key=settings.SECRET_KEY, algorithms=["HS256"])
            except jwt.exceptions.DecodeError:
                raise serializers.ValidationError(code='authorization')
        else:
            raise serializers.ValidationError(code='authorization')
        
        exp_model = [Product, Provider, Industry]
        for iterator in exp_model:
            if iterator.objects.filter(adv_id=adv_id).exists():
                attrs['text_out'] = iterator.objects.get(adv_id=adv_id).text_out
            else:
                continue
        return attrs


'''
attrs['type_services'] = marketing.type_services
        attrs['economic_works'] = marketing.economic_works
        attrs['type_services'] =  type_services'''

'''
class ProviderSerializer(serializers.Serializer):
    id_provider = serializers.CharField(label='id_provider')
    title = serializers.CharField(label='title')
    text_in = serializers.CharField(label='text_in')

    def validate(self, attrs):

class ProviderSerializer(serializers.Serializer):

class ProviderSerializer(serializers.Serializer):
'''
