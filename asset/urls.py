from django.urls import path, include

from asset.views import *

app_name = 'asset'

urlpatterns = [
    path('company/', CompanyListCreateAPIView.as_view(), name='company-list'),
    path('company/<int:pk>/', CompanyRetrieveUpdateDestroyAPIView.as_view(), name='company-detail'),
]