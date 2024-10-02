from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from account.models import CustomUser

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
'''
class ProviderSerializer(serializers.Serializer):
    id_provider = serializers.CharField(label='id_provider')
    title = serializers.CharField(label='title')
    text_in = serializers.CharField(label='text_in')

    def validate(self, attrs):

















class ProviderSerializer(serializers.Serializer):

class ProviderSerializer(serializers.Serializer):
'''  