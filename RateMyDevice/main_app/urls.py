from django.contrib import admin
from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('devices', views.device_index, name='device-ind'),
    path('about/', views.about, name='about'),

    path('device/create/', views.DeviceCreate.as_view(), name='device-create'),
    path('devices/<int:device_id>/', views.device_detail, name='device-detail'),


    # Path for adding review
    path('devices/<int:device_id>/add-review', views.add_review, name='add-review'),
    path('devices/<int:pk>/update/', views.DeviceUpdate.as_view(), name='device-update'),
    path('devices/<int:pk>/delete/', views.DeviceDelete.as_view(), name='device-delete'),
    path('device/<int:pk>/like/', views.device_like, name='device-like'),

    # Signup URL
    path('accounts/signup/', views.signup, name='signup'),

    # Logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]