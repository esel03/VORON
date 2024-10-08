from rest_framework import serializers
from .models import Advertisement
from account.models import CustomUser

from django.conf import settings
import jwt


class CreateAdvertisementAddSerializer(serializers.Serializer):
    token = serializers.CharField(label='token')
    type_services = serializers.CharField(label='type_services')
    platforms = serializers.CharField(label='platforms')
    price = serializers.FloatField(label='price')
    date_start = serializers.DateTimeField(label='date_start', default=None)
    date_finish = serializers.DateTimeField(label='date_finish', default=None)
    economic_works = serializers.CharField(label='economic_works') 
    
    def validate(self, attrs):
        token = attrs.get('token')
        if token:
            try:
                auth = jwt.decode(token, key=settings.SECRET_KEY, algorithms=["HS256"])
            except jwt.exceptions.DecodeError:
                raise serializers.ValidationError(code='authorization')
        else:
            raise serializers.ValidationError(code='authorization')

        users = auth['id_user']
        result_dict = {}
        exp_dict = { 
        'type_services': attrs.get('type_services').lower(), 
        'platforms': attrs.get('platforms').lower(), 
        'price': attrs.get('price'), 
        'date_start': attrs.get('date_start'),
        'date_finish': attrs.get('date_finish'),
        'economic_works': attrs.get('economic_works')
        }

        for key in exp_dict.keys():
            if exp_dict.get(key) != None:
                result_dict.update([(f'{key}', f'{exp_dict.get(key)}')])

        mod = Advertisement.objects.create(users_id=users, **result_dict)
        attrs['auth'] = auth['id_user']
        attrs['adv_id'] = mod.adv_id
        return attrs




class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(label='token')
    #number_interval = serializers.IntegerField(label='number_interval')

    def validate(self, attrs):
        token = attrs.get('token')
        if token:
            try:
                auth = jwt.decode(token, key=settings.SECRET_KEY, algorithms=["HS256"])
            except jwt.exceptions.DecodeError:
                raise serializers.ValidationError(code='authorization')
        else:
            raise serializers.ValidationError(code='authorization')

        attrs['auth'] = auth['id_user']
        return attrs

class DeleteOneAdvertisementSerializer(serializers.Serializer):
    token = serializers.CharField(label='token')
    adv_id = serializers.CharField(label='adv_id')

    def validate(self, attrs):
        token = attrs.get('token')
        adv_id = attrs.get('adv_id')
        if token:
            try:
                auth = jwt.decode(token, key=settings.SECRET_KEY, algorithms=["HS256"])
            except jwt.exceptions.DecodeError:
                raise serializers.ValidationError(code='authorization')
        else:
            raise serializers.ValidationError(code='authorization')

        Advertisement.objects.filter(adv_id=adv_id).delete()
        return attrs


class DeleteListAdvertisementSerializer(serializers.Serializer):
    token = serializers.CharField(label='token')
    adv_id = serializers.CharField()

    def validate(self, attrs):
        token = attrs.get('token')
        adv_id = attrs.get('adv_id')
        print(adv_id)
        if token:
            try:
                auth = jwt.decode(token, key=settings.SECRET_KEY, algorithms=["HS256"])
            except jwt.exceptions.DecodeError:
                raise serializers.ValidationError(code='authorization')
        else:
            raise serializers.ValidationError(code='authorization')

        #for iterator in range(len(adv_id)):
            #print(adv_id[iterator])
            #Advertisement.objects.filter(adv_id=adv_id[iterator]).delete()
        return attrs

class AdvSerializer(serializers.Serializer):
    adv_id = serializers.CharField()

class DeleteDictAdvertisementSerializer(serializers.Serializer):
    token = serializers.CharField(label='token')
    adv = AdvSerializer(many=True)

    def validate(self, attrs):
        token = attrs.get('token')
        adv = attrs.get('adv')
        print(adv)
        if token:
            try:
                auth = jwt.decode(token, key=settings.SECRET_KEY, algorithms=["HS256"])
            except jwt.exceptions.DecodeError:
                raise serializers.ValidationError(code='authorization')
        else:
            raise serializers.ValidationError(code='authorization')

        #for iterator in range(len(adv_id)):
            #print(adv_id[iterator])
            #Advertisement.objects.filter(adv_id=adv_id[iterator]).delete()
        return attrs



class UpdateAdvertisementSerializer(serializers.Serializer):
    token = serializers.CharField(label='token')
    adv_id = serializers.CharField(label='adv_id')
    title = serializers.CharField(label='title', default=None)
    platforms = serializers.CharField(label='platforms', default=None)
    price = serializers.FloatField(label='price', default=None)

    def validate(self, attrs):
        token = attrs.get('token')
        adv_id = attrs.get('adv_id')
        price = attrs.get('price')
        if token:
            try:
                auth = jwt.decode(token, key=settings.SECRET_KEY, algorithms=["HS256"])
            except jwt.exceptions.DecodeError:
                raise serializers.ValidationError(code='authorization')
        else:
            raise serializers.ValidationError(code='authorization')

        result_dict = {}
        exp_dict = {
            'title': attrs.get('title'), 
            'platforms': attrs.get('platforms'),
            'price': attrs.get('price')
            }

        for key in exp_dict.keys():
            if exp_dict.get(key) != None:
                result_dict.update([(f'{key}', f'{exp_dict.get(key)}')])

        user_adv = Advertisement.objects.get(adv_id=adv_id)
        if user_adv.status_first_start or user_adv.status_done == True:
            Advertisement.objects.update(**result_dict)
        else:
            attrs['update_data'] = '0'
        attrs['update_data'] = '1'
        return attrs





'''
users = attrs.get('auth'), 
                type_services = attrs.get('type_services'), 
                platforms = attrs.get('platforms'), 
                price = attrs.get('price'), 
                date_start = attrs.get('date_start'),
                date_finish = attrs.get('date_finish'),
                economic_works = attrs.get('economic_works')


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(label='token')
    
    def validate(self, attrs):
        token = attrs.get('token')
        if token:
            try:
                auth = jwt.decode(token, key=settings.SECRET_KEY, algorithms=["HS256"])
            except jwt.exceptions.DecodeError:
                raise serializers.ValidationError(code='authorization')
        else:
            raise serializers.ValidationError(code='authorization')
        attrs.pop('token')
        attrs['auth'] = auth['id_user']
        return attrs
'''


'''
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZF91c2VyIjoiYmFmYmQzMWQtMjhmYS00OThiLTgzY2UtMzdkZTg5MjVmMTc2IiwiaWF0IjoxNzI3OTE2Mzk2LCJuYmYiOjE3Mjc5MTYwOTYsImV4cCI6MTczMDUwODM5Nn0.29R9Cr7alkC3bZXDz6ynmYGsJ2yJmhm8dwrKp1FzM7I",
"adv": [ {"adv_id":"ef5e3dded89747589f75ead0ff208c15"}, {"adv_id":"5f21c4ee6aea41f2b02f1bf9432030c8"}, {"adv_id":"5ad2fbfe1ae143dc8d0287443c72a355"}, {"adv_id":"a894852db7fe43afa6c67e4505f25f01"}]
}
'''









