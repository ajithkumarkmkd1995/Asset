from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from asset.views import AssetsModel

from asset.serializers import AssetSerializer

ASSETS_URL = reverse('asset:asset-list')


def detail_url(asset_id):
  """ Return asset details url """
  return reverse('asset:asset-detail', args=[asset_id])

def sample_asset(name="test name", manufacturer="test manu", condition = "good" ):
  """ Create sample asset object """
  return AssetsModel.objects.create(name=name, manufacturer=manufacturer, condition=condition)


class assetApiTest(TestCase):
  """ Test the asset api """
  
  def setUp(self):
    self.client = APIClient()
  
  def test_list_assets(self):
    """ Test list assets successfully"""
    sample_asset(name="test name", manufacturer="test manu", condition = "good" )
    sample_asset(name="test name2", manufacturer="test manu2", condition = "good2" )
    
    res = self.client.get(ASSETS_URL)
    
    asset= AssetsModel.objects.all()
    serializer = AssetSerializer(asset, many=True)
    
    self.assertEqual(res.status_code, status.HTTP_200_OK)
    self.assertEqual(res.data, serializer.data)
  
  def test_create_assets_successfuly(self):
    """ test that assets is created successfully"""
    asset = sample_asset()
    payload = {
      'name': "test name",
      'manufacturer' : "test manu",
      'condition' : "good"
      }
    
    res = self.client.post(ASSETS_URL, payload)
    
    exists = AssetsModel.objects.filter(
      name = payload['name'],
      manufacturer = payload['manufacturer'],
      condition = payload['condition']
    ).exists()
    
    self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    self.assertTrue(exists)
  
  
  def test_retrieve_asset(self):
    """ test retrieving asset details """
    asset = sample_asset()
    
    url = detail_url(asset.id)
    res = self.client.get(url)
    
    self.assertEqual(res.status_code, status.HTTP_200_OK)
    self.assertEqual(res.data['name'], sample_asset().name)
    self.assertEqual(res.data['manufacturer'], sample_asset().manufacturer)
  
  
  def test_partial_update_asset(self):
    """ Test updating a asset with patch """
    asset = sample_asset()
    payload = {'name': 'Updated asset'}
    
    url = detail_url(asset.id)
    res = self.client.patch(url, payload)
    
    asset.refresh_from_db()
    
    self.assertEqual(res.status_code, status.HTTP_200_OK)
    self.assertEqual(asset.name , payload['name'])
    self.assertEqual(asset.manufacturer , sample_asset().manufacturer)
  
  
  def test_delete_employee(self):
    """ Test deleting a asset  """
    asset = sample_asset()
    
    url = detail_url(asset.id)
    res = self.client.delete(url)
    
    self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
    self.assertEqual(AssetsModel.objects.count(), 0)

