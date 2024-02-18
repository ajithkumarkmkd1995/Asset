from rest_framework import serializers

from asset.models import *

class CompanySerializer(serializers.ModelSerializer):
  """ Serializer for company object """

  class Meta :
    model = CompanyModel
    fields = ('id','name','address')
    read_only_fields = ('id',)


class EmployeeSerializer(serializers.ModelSerializer):
  """ Serializer for employee object """
  class Meta :
    model = EmployeeModel
    fields = ('id', 'name', 'department', 'company')
    read_only_fields = ('id',)
    



class AssetSerializer(serializers.ModelSerializer):
  """ Serializer for asset object """
  class Meta :
    model = AssetsModel
    fields = ('id', 'name', 'manufacturer', 'purchased_date', 'condition', 'issued')
    read_only_fields = ('id','issued')


class AssetsLogSerializer(serializers.ModelSerializer):
  """ Serializer for Assets Log object """
  asset = serializers.StringRelatedField(read_only = True)
  employee = serializers.StringRelatedField(read_only = True)
  
  class Meta:
    model = AssetsLogModel
    fields = ('id', 'asset', 'employee', 'checkout_date', 'checkout_condition', 'return_date', 'return_condition')
    read_only_fields = ('id',)

class AssetsLogCreateSerializer(serializers.ModelSerializer):
  """ Serializer for Assets Log Create object """
  class Meta:
    model = AssetsLogModel
    fields = ('id', 'asset', 'employee', 'checkout_date', 'checkout_condition', 'return_date', 'return_condition')
    read_only_fields = ('id',)
