from django.urls import path
from . import views 
urlpatterns = [
    path('', views.home, name='home'),
    path('', views.device_index, name='home'),
    path('about/', views.about, name='about'),

    # CBV's for CREATE, UPDATE, and Delete
]