from rest_framework import viewsets
from rest_framework import generics
from asset.models import *

from asset import serializers
# Create your views here.

class CompanyListCreateAPIView(generics.ListCreateAPIView):
  """ API view for listing and creating companies """
  queryset = CompanyModel.objects.all()
  serializer_class = serializers.CompanySerializer

class CompanyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  """ API view for retrieving, updating, and deleting a company """
  queryset = CompanyModel.objects.all()
  serializer_class = serializers.CompanySerializer

