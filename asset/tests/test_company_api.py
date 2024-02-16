from django.urls import reverse
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status

from asset.serializers import CompanySerializer
from asset.models import CompanyModel

COMPANY_URL = reverse('asset:company-list')

def detail_url(company_id):
  """ Return company details url """
  return reverse('asset:company-detail', args=[company_id])

def sample_company(name='test company', address='test address'):
  """ Create sample company object """
  return CompanyModel.objects.create(name=name, address=address)


class CompanyApiTest(TestCase):
  """ Test the company api """
  
  def setUp(self):
    self.client = APIClient()
  
  def test_list_companies(self):
    """ Test list companies successfully"""
    sample_company(name='test company', address='test area')
    sample_company(name='test company2', address='test area2')
    
    res = self.client.get(COMPANY_URL)
    
    company= CompanyModel.objects.all()
    serializer = CompanySerializer(company, many=True)
    
    self.assertEqual(res.status_code, status.HTTP_200_OK)
    self.assertEqual(res.data, serializer.data)
  
  def test_create_company_successfuly(self):
    """ test that company is created successfully"""
    payload = {'name': "test company", 'address' : "test area"}
    res = self.client.post(COMPANY_URL, payload)
    
    exists = CompanyModel.objects.filter(
      name = payload['name'],
      address = payload['address'],
    ).exists()
    
    self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    self.assertTrue(exists)
  
  def test_create_company_invalid(self):
    """ test creating company with invalid payload """
    payload = {'name': ''}
    res = self.client.post(COMPANY_URL, payload)
    
    self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
  
  def test_retrieve_company(self):
    """ test retrieving company details """
    company = sample_company()
    
    url = detail_url(company.id)
    res = self.client.get(url)
    
    self.assertEqual(res.status_code, status.HTTP_200_OK)
    self.assertEqual(res.data['name'], sample_company().name)
    self.assertEqual(res.data['address'], sample_company().address)
  
  def test_partial_update_company(self):
    """ Test updating a company with patch """
    company = sample_company()
    payload = {'name': 'Updated Company'}
    
    url = detail_url(company.id)
    res = self.client.patch(url, payload)
    
    company.refresh_from_db()
    
    self.assertEqual(res.status_code, status.HTTP_200_OK)
    self.assertEqual(company.name , payload['name'])
    self.assertEqual(company.address , sample_company().address)
