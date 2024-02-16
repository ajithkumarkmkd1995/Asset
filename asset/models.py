from django.db import models
from django.utils import timezone

# Create your models here.



class CompanyModel(models.Model):
  """ Model for company table """
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=255)
  
  def __str__(self):
    return self.name


class EmployeeModel(models.Model):
  """ Model for employee table """
  name = models.CharField(max_length=100)
  department = models.CharField(max_length=100)
  company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, related_name= 'employe',)
  
  def __str__(self):
      return self.name


class AssetsModel(models.Model):
  """ Model for Assets detials table  """
  name  = models.CharField(max_length=50)
  manufacturer  = models.CharField(max_length=100)
  purchased_date = models.DateTimeField(default=timezone.now)
  condition = models.TextField()
  issued = models.BooleanField(default=False)
  
  def __str__(self) -> str:
    return f"{self.name} by {self.manufacturer}"


class AssetsLogModel(models.Model):
  """ Model for assets log info table """
  asset = models.ForeignKey(AssetsModel, on_delete=models.CASCADE, related_name = 'asset')
  employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE, related_name = 'employee')
  checkout_date = models.DateTimeField()
  checkout_condition = models.TextField()
  return_date = models.DateTimeField()
  return_condition = models.TextField()