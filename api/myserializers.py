from rest_framework import serializers
from .models import *

class CLimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Climate
        fields = '__all__'