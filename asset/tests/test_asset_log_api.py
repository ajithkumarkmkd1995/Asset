from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from asset.models import CompanyModel, AssetsLogModel, AssetsModel, EmployeeModel
from asset.serializers import AssetsLogSerializer 

ASSETLOG_URL = reverse('asset:assets-logs-list')


def detail_url(asset_log_id):
  """ Return asset_log details url """
  return reverse('asset:assets-logs-detail', args=[asset_log_id])


def sample_company(name='test company', address='test address'):
  """ Create sample company object """
  return CompanyModel.objects.create(name=name, address=address)

def sample_employee(name='test employee', department='test department'):
  """ Create sample employee object """
  company = sample_company()
  return EmployeeModel.objects.create(name=name, department=department, company=company)

def sample_asset(name="test name", manufacturer="test manu", condition = "good" ):
  """ Create sample asset object """
  return AssetsModel.objects.create(name=name, manufacturer=manufacturer, condition=condition)

def sample_asset_log():
  """ Create sample asset log object """
  return AssetsLogModel.objects.create(
      asset=sample_asset(), 
      employee=sample_employee(), 
      checkout_condition='Test Checkout Condition', 
      return_date='2022-02-17', 
      return_condition='Test Return Condition'
    )




class AssetsLogAPITest(TestCase):
  """ Test the asset log api """
  
  def setUp(self):
    self.client = APIClient()
    self.asset = sample_asset()
    self.employee = sample_employee()
    self.payload = {
      'asset': self.asset.pk,
      'employee': self.employee.id,
      'checkout_condition': 'Test Checkout Condition',
      'return_date' : '2022-02-17',
      'return_condition': 'Test Return Condition'
      }
    
  def test_list_assets(self):
    """ Test list assets log successfully"""
    sample_asset_log()
    
    res = self.client.get(ASSETLOG_URL)
    
    asset_log= AssetsLogModel.objects.all()
    serializer = AssetsLogSerializer(asset_log, many=True)
    
    self.assertEqual(res.status_code, status.HTTP_200_OK)
    self.assertEqual(res.data, serializer.data)
  
  
  def test_create_already_issued_asset_log(self):
    """ Test Mark the asset as issued True """
    asset = sample_asset()
    asset.issued = True
    asset.save()
    
    res = self.client.post(ASSETLOG_URL, self.payload)
    
    # self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
    # self.assertEqual(AssetsLogModel.objects.count(), 0)
  
  def test_create_assets_successfuly(self):
    """ test that assets is created successfully"""
    

    res = self.client.post(ASSETLOG_URL, self.payload)
    
    exists = AssetsLogModel.objects.filter(
      asset = self.payload['asset']
    ).exists()
    
    self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    self.assertTrue(exists)
  
  def test_update_assets_log(self):
    """ Test updating a asset with patch """
    asset_log = sample_asset_log()
    
    updated_data = {'return_condition': 'Updated Return Condition'}
    
    url = detail_url(asset_log.id)
    res = self.client.patch(url, updated_data)
    
    self.assertEqual(res.status_code, status.HTTP_200_OK)
    self.assertEqual(res.data['return_condition'], updated_data['return_condition'])
  
  
  def test_delete_assets_log(self):
    """ Test deleting a asset  """
    asset_log = sample_asset_log()
    
    url = detail_url(asset_log.id)
    res = self.client.delete(url)
    
    self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
    self.assertEqual(AssetsLogModel.objects.count(), 0)
