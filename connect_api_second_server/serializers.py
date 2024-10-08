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
        type_services = attrs.get('type_services')
        if token:
            try:
                auth = jwt.decode(token, key=settings.SECRET_KEY, algorithms=["HS256"])
            except jwt.exceptions.DecodeError:
                raise serializers.ValidationError(code='authorization')
        else:
            raise serializers.ValidationError(code='authorization')
        if type_services == 'услуга': #provider
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

        elif type_services == 'товар': #product
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
        else: #industry
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
        adv_id = attrs.get('type_services')
        if token:
            try:
                auth = jwt.decode(token, key=settings.SECRET_KEY, algorithms=["HS256"])
            except jwt.exceptions.DecodeError:
                raise serializers.ValidationError(code='authorization')
        else:
            raise serializers.ValidationError(code='authorization')

        marketing = Advertisement.objects.get(pk=adv_id)
        type_services = marketing.type_services
        exp_dict = {
            "economic_works": f'{marketing.economic_works}',
            "type_services": f'{type_services}',
            }
        if type_services == 'услуга':
            marketing_twotable = Provider.objects.get(pk=adv_id)
            exp_dict.update([(f'{title}', f'{marketing_twotable.title}')])





































'''
class ProviderSerializer(serializers.Serializer):
    id_provider = serializers.CharField(label='id_provider')
    title = serializers.CharField(label='title')
    text_in = serializers.CharField(label='text_in')

    def validate(self, attrs):

















class ProviderSerializer(serializers.Serializer):

class ProviderSerializer(serializers.Serializer):
'''  