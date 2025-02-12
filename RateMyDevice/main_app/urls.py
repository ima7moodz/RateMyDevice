from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('devices', views.device_index, name='device-ind'),
    path('about/', views.about, name='about'),

    path('device/create/', views.DeviceCreate.as_view(), name='device-create'),
    path('devices/<int:device_id>/', views.device_detail, name='device-detail'),
    path('devices/<int:pk>/update/', views.DeviceUpdate.as_view(), name='device-update'),
    path('devices/<int:pk>/delete/', views.DeviceDelete.as_view(), name='device-delete'),
    path('device/<int:pk>/like/', views.device_like, name='device-like'),
]