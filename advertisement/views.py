from django.shortcuts import render
from rest_framework import parsers, renderers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Advertisement
from account.models import CustomUser
from .serializers import CreateUserCustomAddSerializer
from django.core.cache import cache


class CreateUserCustomAdd(APIView):
    serializer_class = CreateUserCustomAddSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        




















