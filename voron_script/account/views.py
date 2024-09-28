import datetime
import jwt
from django.conf import settings
from rest_framework import parsers, renderers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomAuthTokenSerializer, CustomUserRegistrationSerializer, UpdateCustomUserSerializer
from .models import CustomUser

class Registration(APIView):

    def post(self, request, format=None):
        serializer = CustomUserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WebTokenAuth(APIView):
    throttle_classes = ()
    permission_classes = ()
    # parser_classes = (parsers.FormParser,parsers.MultiPartParser, parsers.JSONParser,)
    # renderer_classes = (renderers.JSONRenderer,)
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token = jwt.encode({
                'id_user': str(user.id_user),
                'iat': datetime.datetime.utcnow(),
                'nbf': datetime.datetime.utcnow() + datetime.timedelta(minutes=-5),
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)
            }, settings.SECRET_KEY, algorithm="HS256")
            return Response({'token': token})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Update_user(APIView):
    serializer_class = UpdateCustomUserSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            user = serializer.upgrade(data)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

















