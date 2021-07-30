from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .myserializers import *

class Countries(APIView):
    def get(self, request):
        data = Climate.objects.all()
        ser = CLimateSerializer(data, many=True)
        return Response(ser.data)

class CountriesFilter(APIView):
    def get(self, request, pk):
        print(pk)
        print(request.GET)
        return Response({'mag':'yes'})