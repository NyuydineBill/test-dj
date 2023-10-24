from django.urls import path 
from . import views 

from rest_framework import viewsets


urlpatterns = [
    path('home',views.EmissionsViewSet.as_view({'get': 'list'}), name='emission')
]