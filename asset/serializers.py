from rest_framework import serializers

from asset.models import *

class CompanySerializer(serializers.ModelSerializer):
  """ Serializer for company object """
  class Meta :
    model = CompanyModel
    fields = ('id','name','address')
    read_only_fields = ('id',)