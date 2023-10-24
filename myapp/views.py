from django.shortcuts import render
from .serializers import EmissionsSerializer
from .models import Emissions
from rest_framework import viewsets


# Create your views here.


class EmissionsViewSet(viewsets.ModelViewSet):
    queryset = Emissions.objects.all()
    serializer_class = EmissionsSerializer