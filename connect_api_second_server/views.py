from django.shortcuts import render
import requests
from rest_framework import parsers, renderers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ConnectSerializer, CreateUnderTableAdvertisementSerializer, TakeMarketingSpecificSerializer, UpdateUnderTableAdvertisementSerializer, TextAdvertisementOutputSerializer
import json
from .models import Provider, Product, Industry

url = "http://127.0.0.1:8001/api/"
headers = {
    "Content-Type": "application/json",
    "Accept-Charset": "UTF-8"
    # "Authorization": "4506"
}


class Connect(APIView):
    serializer_class = ConnectSerializer

    def post(self, request, format=None):
        prompt = {
            "id_user": request.data['id_user'],
            "entry": request.data['entry']
        }
        result = requests.post(url, headers=headers, json=prompt)
        json_text = json.loads(result.text)
        print(json_text)
        return Response({"id_user": json_text["id_user"], "out": json_text["out"]})


class CreateUnderTableAdvertisement(APIView):
    serializer_class = CreateUnderTableAdvertisementSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():

            return Response(serializer.validated_data['auth']['id_user'], status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class TakeMarketingSpecific(APIView):
    serializer_class = TakeMarketingSpecificSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            attrs = serializer.validated_data
            return Response(attrs, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UpdateUnderTableAdvertisement(APIView):
    serializer_class = UpdateUnderTableAdvertisementSerializer

    def post(self, request, fomat=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            

class TextAdvertisementOutput(APIView):
    serializer_class = TextAdvertisementOutputSerializer
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data['text_out'], status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)              
                   


# requests.post(url, headers=headers, json=prompt)
'''
serializer = self.serializer_class(data=result.json().data)
        if serializer.is_valid():
            return Response(result.json())
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
            {"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZF91c2VyIjoiYmFmYmQzMWQtMjhmYS00OThiLTgzY2UtMzdkZTg5MjVmMTc2IiwiaWF0IjoxNzI4NDIxMjY4LCJuYmYiOjE3Mjg0MjA5NjgsImV4cCI6MTczMTAxMzI2OH0.2ErlQtunDQnh9X9DsNUMxiZIWZ9zE-eXxGuS9ppP3m8",
"adv_id":"5ad2fbfe1ae143dc8d0287443c72a355",
"text_out":"Биба плохо"
}
'''


'''
prompt = {
        "id_user": "gpt://b1g7in2c2dp5md2dei6m/yandexgpt-lite",
        "entry": 

url = "http://127.0.0.1:8000/api/"

headers = {
        "Content-Type": "application/json",
        "Authorization": "4506"
    }
'''
# Create your views here.
