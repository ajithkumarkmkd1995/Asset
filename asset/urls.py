from django.urls import path, include

from rest_framework.routers import DefaultRouter

from asset.views import *

app_name = 'asset'

router = DefaultRouter()
router.register('companies', CompanyAPIViewSet, basename='company')
router.register('employees', EmployeeAPIViewSet, basename='employee')
router.register('assets', AssetsAPIViewSet, basename='asset')
router.register('assets-logs', AssetsLogAPIView , basename='assets-logs')

urlpatterns = [
    path('', include(router.urls)),
]
