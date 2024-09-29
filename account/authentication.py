import jwt
from django.conf import settings
from .models import AbstractUser
from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication


class JSONWebTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        try:
            payload = jwt.decode(key, settings.SECRET_KEY)
            user = AbstractUser.objects.get(email=payload['email'])
        except (jwt.DecodeError, AbstractUser.DoesNotExist):
            raise exceptions.AuthenticationFailed('Invalid token')
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token has expired')
        if not user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted')
        return (user, payload)
