from django.test import TestCase


from asset import models

def sample_company(name='test company', address='test area'):
  """ Create sample company object """
  return models.CompanyModel.objects.create(name=name, address=address)

class ModelTest(TestCase):
  """ Test app Models """
  
  def test_company_str(self):
    """ Test company model string representation """
    company = models.CompanyModel.objects.create(
      name = 'test company',
      address = 'test area'
    )
    
    self.assertEqual(str(company), company.name)
  
  def test_employee_str(self):
    """ Test employee model string representation """
    employee = models.EmployeeModel.objects.create(
      name = 'test name',
      department = 'test department',
      company = sample_company()
    )
    
    self.assertEqual(str(employee), employee.name)
  
  def test_assets_str(self):
    """ Test assets model string representation """
    asset = models.AssetsModel.objects.create(
      name = 'test asset name',
      manufacturer = 'test manufacturer',
      condition = 'good'
    )
    
    self.assertEqual(str(asset), f'{asset.name} by {asset.manufacturer}')
  
  