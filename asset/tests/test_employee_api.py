from django.urls import reverse
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status

from asset.serializers import EmployeeSerializer
from asset.models import CompanyModel, EmployeeModel

EMPLOYEE_URL = reverse('asset:employee-list')

def detail_url(employee_id):
  """ Return employee details url """
  return reverse('asset:employee-detail', args=[employee_id])

def sample_company(name='test company', address='test address'):
  """ Create sample company object """
  return CompanyModel.objects.create(name=name, address=address)

def sample_employee(name='test employee', department='test department'):
  """ Create sample employee object """
  company = sample_company()
  return EmployeeModel.objects.create(name=name, department=department, company=company)


class EmployeeApiTest(TestCase):
  """ Test the employee api """
  
  def setUp(self):
    self.client = APIClient()
  
  def test_list_employees(self):
    """ Test list companies successfully"""
    sample_employee(name='test employee', department='test department')
    sample_employee(name='test employee2', department='test department2')
    
    res = self.client.get(EMPLOYEE_URL)
    
    employee= EmployeeModel.objects.all()
    serializer = EmployeeSerializer(employee, many=True)
    
    self.assertEqual(res.status_code, status.HTTP_200_OK)
    self.assertEqual(res.data, serializer.data)
  
  def test_create_employee_successfuly(self):
    """ test that employee is created successfully"""
    company = sample_company()
    payload = {
      'name': "test employee",
      'department' : "test department",
      'company' : company.id
      }
    
    res = self.client.post(EMPLOYEE_URL, payload)
    
    exists = EmployeeModel.objects.filter(
      name = payload['name'],
      department = payload['department'],
    ).exists()
    
    self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    self.assertTrue(exists)
  
  def test_create_employee_invalid(self):
    """ test creating employee with invalid payload """
    payload = {'name': ''}
    res = self.client.post(EMPLOYEE_URL, payload)
    
    self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
  
  def test_retrieve_employee(self):
    """ test retrieving employee details """
    employee = sample_employee()
    
    url = detail_url(employee.id)
    res = self.client.get(url)
    
    self.assertEqual(res.status_code, status.HTTP_200_OK)
    self.assertEqual(res.data['name'], sample_employee().name)
    self.assertEqual(res.data['department'], sample_employee().department)
  
  def test_partial_update_employee(self):
    """ Test updating a employee with patch """
    employee = sample_employee()
    payload = {'name': 'Updated Employee'}
    
    url = detail_url(employee.id)
    res = self.client.patch(url, payload)
    
    employee.refresh_from_db()
    
    self.assertEqual(res.status_code, status.HTTP_200_OK)
    self.assertEqual(employee.name , payload['name'])
    self.assertEqual(employee.department , sample_employee().department)
