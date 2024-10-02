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
    date_start = serializers.DateTimeField(label='date_start')
    date_finish = serializers.DateTimeField(label='date_finish')
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
        exp_dict = { 
        'type_services': attrs.get('type_services').lower(), 
        'platforms': attrs.get('platforms').lower(), 
        'price': attrs.get('price'), 
        'date_start': attrs.get('date_start'),
        'date_finish': attrs.get('date_finish'),
        'economic_works': attrs.get('economic_works')
        }

        for key in exp_dict.keys():
            if exp_dict.get(key) == None:
                raise serializers.ValidationError(code='authorization') 

        mod = Advertisement.objects.create(users_id=users, **exp_dict)
        attrs['auth'] = auth['id_user']
        attrs['id_adv'] = mod.users_id
        return attrs




class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(label='token')
    number_interval = serializers.IntegerField(label='number_interval')

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













