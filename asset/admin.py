from django.contrib import admin
from asset import models
# Register your models here.

admin.site.register(models.CompanyModel)
admin.site.register(models.EmployeeModel)
admin.site.register(models.AssetsModel)
admin.site.register(models.AssetsLogModel)