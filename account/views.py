import datetime
import jwt
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.conf import settings
from rest_framework import parsers, renderers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomAuthTokenSerializer, CustomUserRegistrationSerializer, UpdateCustomUserSerializer, TokenSerializer, EmailSerializer
from .models import CustomUser



class BeforeRegistration(APIView):
    serializer_class = EmailSerializer

    def post(self, request, format=None):
        secret_key = random.randint(10000, 99999)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email_user = serializer.validated_data['email']
            fromaddr = "voron_script@mail.ru"
            toaddr = f"{email_user}"
            mypass = "Q9xuBRVJa2T5GctLhFyq"
 
            msg = MIMEMultipart('alternative')
            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = "Привет от Voron Script!"
 
            s1 = """
            <!DOCTYPE html>
            <html lang="ru">
            <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Подтверждение регистрации</title>
            </head>
            <body>
            <div class="container">
                <h1>Код подтверждения:""" 

            s2 = """ </h1></div></body></html>"""
            s3 = f'{secret_key}'
            body = s1 + s2 + s3

            msg.attach(MIMEText(body, 'html'))
 
            server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
            server.login(fromaddr, mypass)
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()

            token_registration = jwt.encode({
                'secret_key': str(secret_key),
                'iat': datetime.datetime.utcnow(),
                'nbf': datetime.datetime.utcnow() + datetime.timedelta(minutes=-5),
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
            }, settings.SECRET_KEY, algorithm="HS256")
            return Response({"token_registration": token_registration}, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Registration(APIView):
    serializer_class = CustomUserRegistrationSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            token_registration = serializer.validated_data["token_registration"]
            if token_registration == serializer.validated_data['key_mail']:
                user = serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30)
            }, settings.SECRET_KEY, algorithm="HS256")
            return Response({'token': token}, status=status.HTTP_200_OK)
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

class View_data(APIView):
    serializer_class = TokenSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data['auth']
            user = CustomUser.objects.get(pk=data)
            response_json = {
            "email": user.email, 
            "first_name": user.first_name, 
            "second_name": user.second_name, 
            "last_name": user.last_name
            }
            return Response(response_json, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
class Delete_account(APIView):
    serializer_class = TokenSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data['auth']
            user = CustomUser.objects.get(pk=data)
            user.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

















