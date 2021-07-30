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
        data = request.GET
        odata = Climate.objects.filter(country_or_area=pk)
        if 'startYear' in data and 'endYear'in data and 'cat'in data:
            print('3')
            odata = Climate.objects.filter(country_or_area=pk, year__gte=int(data['startYear']), year__lte=int(data['endYear']), category=data['cat']) 
        elif 'startYear' in data and 'endYear'in data:
            print('2')
            print(data['startYear'])
            print(data['endYear'])
            odata = Climate.objects.filter(country_or_area=pk, year__gte=int(data['startYear']), year__lte=int(data['endYear']))
        elif 'startYear' in data and 'cat'in data:
            print('1')
            odata = Climate.objects.filter(country_or_area=pk, year__gte=int(data['startYear']), category=data['cat']) 
        elif 'cat'in data:
            print('0')
            odata = Climate.objects.filter(country_or_area=pk, category=data['cat']) 
        elif 'startYear'in data:
            print('0')
            odata = Climate.objects.filter(country_or_area=pk, year__gte=int(data['startYear'])) 

        ser = CLimateSerializer(odata, many=True)
        return Response(ser.data)