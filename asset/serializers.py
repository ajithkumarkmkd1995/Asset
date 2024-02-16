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