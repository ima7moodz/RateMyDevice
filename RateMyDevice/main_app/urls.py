from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('device/create/', views.DeviceCreate.as_view(), name='device-create'),
]