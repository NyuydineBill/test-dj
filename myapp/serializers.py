from rest_framework import serializers
from .models import Emissions

class EmissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emissions
        fields = '__all__'