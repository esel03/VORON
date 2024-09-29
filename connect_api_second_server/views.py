from django.shortcuts import render
import requests
from rest_framework import parsers, renderers, status
from rest_framework.response import Response

#from curl_cffi import requests
from rest_framework.views import APIView
from .serializers import ConnectSerializer
import json

url = "http://127.0.0.1:8001/api/"
headers = {
        "Content-Type": "application/json",
        "Accept-Charset": "UTF-8"
        #"Authorization": "4506"
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
        

#requests.post(url, headers=headers, json=prompt)


'''
serializer = self.serializer_class(data=result.json().data)
        if serializer.is_valid():
            return Response(result.json())
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
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
