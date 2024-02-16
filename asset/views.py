from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from asset.models import *

from asset import serializers
# Create your views here.


class CompanyAPIViewSet(viewsets.ModelViewSet):
  """ API view for listing, creating, retrieving, updating, and deleting a company """
  queryset = CompanyModel.objects.all()
  serializer_class = serializers.CompanySerializer


class EmployeeAPIViewSet(viewsets.ModelViewSet):
  """ API view for listing, creating, retrieving, updating, and deleting a emoloyee """
  queryset = EmployeeModel.objects.all()
  serializer_class = serializers.EmployeeSerializer


class AssetsAPIViewSet(viewsets.ModelViewSet):
  """ API view for listing, creating, retrieving, updating, and deleting assets """
  queryset = AssetsModel.objects.all()
  serializer_class = serializers.AssetSerializer

