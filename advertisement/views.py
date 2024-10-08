from django.shortcuts import render
from rest_framework import parsers, renderers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Advertisement
from account.models import CustomUser
from .serializers import CreateAdvertisementAddSerializer, TokenSerializer, UpdateAdvertisementSerializer, DeleteDictAdvertisementSerializer
from django.core.cache import cache


class CreateAdvertisementAdd(APIView):
    serializer_class = CreateAdvertisementAddSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            advertisement = serializer.validated_data['adv_id']
            return Response(advertisement, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

class TakeAdvertisementList(APIView):
    serializer_class = TokenSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            customuser_id = serializer.validated_data['auth']
            #number_interval = serializer.validated_data['number_interval']
            send_advertisement = Advertisement.objects.filter(users=customuser_id).all()
            result_dict = {}
            iterator = 0
            for take_info in send_advertisement:
                result_dict.update({
                    f'Advertisement_{iterator}': {
                        'adv_id': f'{take_info.adv_id}',
                        'title': f'{take_info.title}',
                        'type_services': f'{take_info.type_services}',
                        'platforms': f'{take_info.platforms}',
                        'status_paid': f'{take_info.status_paid}',
                        'price': f'{take_info.price}',
                        'status_done': f'{take_info.status_done}',
                        'date_create': f'{take_info.date_create}',
                        'date_start': f'{take_info.date_start}',
                        'date_finish': f'{take_info.date_finish}',
                        'economic_works': f'{take_info.economic_works}',
                        'status_first_start': f'{take_info.status_first_start}'
                        }
                    })
                iterator+=1
            
            return Response(result_dict, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class DeleteAdvertisement(APIView):
    serializer_class_list = DeleteDictAdvertisementSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class_list(data=request.data)
        if serializer.is_valid():
            return Response(status=status.HTTP_200_OK)
        else:
            return Response('Пасько', status=status.HTTP_400_BAD_REQUEST)



class UpdateAdvertisement(APIView):
    serializer_class = UpdateAdvertisementSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            if serializer.validated_data['update_data'] == 0:
                return Response(status=status.HTTP_412_PRECONDITION_FAILED)
            else:
                return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)





'''
class DeleteAdvertisement(APIView):
    serializer_class_one = DeleteOneAdvertisementSerializer
    serializer_class_list = DeleteListAdvertisementSerializer

    def post(self, request, format=None):
        if type(request.data['adv_id']) == str:
            print(request.data)
            print(type(request.data['adv_id']))
            serializer = self.serializer_class_one(data=request.data)
            if serializer.is_valid():
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = self.serializer_class_list(data=request.data)
            if serializer.is_valid():
                return Response(status=status.HTTP_200_OK)
            else:
                return Response('Пасько', status=status.HTTP_400_BAD_REQUEST)
'''








