from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager
import jwt

class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name',
                  'second_name', 'last_name', 'password']

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            second_name=validated_data['second_name'],
            last_name=validated_data['last_name'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(
        label=_("Email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

class UpdateCustomUserSerializer(serializers.Serializer):
    token = serializers.CharField(label='token')
    email = serializers.EmailField(label='email', default=None)
    password = serializers.CharField(label='password', default=None)
    first_name = serializers.CharField(label='first_name', default=None)
    second_name = serializers.CharField(label='second_name', default=None)
    last_name = serializers.CharField(label='last_name', default=None)

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

    def upgrade(self, attrs):
        exp_dict = {
        "email": attrs.get('email'), 
        "first_name": attrs.get('first_name'),
        "second_name": attrs.get('second_name'),
        "last_name": attrs.get('last_name')
        }
        result_dict = {}
        for key in exp_dict.keys():
            if exp_dict.get(key) != None:
                result_dict.update([(f'{key}', f'{exp_dict.get(key)}')])
        if attrs.get('password'):
            new_password = CustomUser.objects.get(pk=attrs['auth'])
            new_password.set_password(attrs.get('password'))
            new_password.save()


        user = CustomUser.objects.filter(pk=attrs['auth']).update(**result_dict)
        return result_dict

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

        attrs['auth'] = auth['id_user']
        return attrs













# {'email': f'data.{email}', 'first_name': f'data.{first_name}', 'second_name': f'data.{second_name}', 'last_name': f'data.{last_name}', 'password': f'data.{password}'}

# {"email":"ega@mail.ru", "first_name":"ivan", "second_name":"stan", "last_name":"egarmin", "password":"1234"}
