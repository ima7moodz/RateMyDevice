from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('', views.home, name='home'),
    path('devices', views.device_index, name='device-ind'),
    path('about/', views.about, name='about'),

    # CBV's for CREATE, UPDATE, and Delete
    path('device/create/', views.DeviceCreate.as_view(), name='device-create'),
]