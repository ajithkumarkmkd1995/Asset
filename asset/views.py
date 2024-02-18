from django.shortcuts import get_object_or_404

from rest_framework import viewsets, mixins 
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status

from asset.models import *

from asset import serializers

from django_filters.rest_framework import DjangoFilterBackend as filter
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


class AssetsLogAPIView(viewsets.GenericViewSet, 
                      mixins.CreateModelMixin, 
                      mixins.ListModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,):
  """ API view for manage assets log """
  queryset = AssetsLogModel.objects.all()
  serializer_class = serializers.AssetsLogSerializer
  """ this view is for filter the assets log based on the employee and company """
  filter_backends = [filter]
  filterset_fields = ['employee','employee__company']
  
  def get_serializer_class(self):
    """ return appropiate serializer class for different action """
    if self.action == 'create':
      return serializers.AssetsLogCreateSerializer
    
    return self.serializer_class
  
  def perform_create(self, serializer):
    # checking is the asset is already deleged to any employee by asset_issued status 
    asset= serializer.validated_data.get('asset')
    if asset.issued:
      print(asset.issued)
      return Response({'detail' : "Cannot delegate an already issued asset."}, status=status.HTTP_400_BAD_REQUEST)
    else:
      asset.issued = True
      asset.save()
    return super().perform_create(serializer)









