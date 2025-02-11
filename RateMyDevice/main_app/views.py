from django.shortcuts import render
from django.http import HttpResponse
from .models import Device
from django.views.generic import CreateView, UpdateView,DeleteView
from django.views.generic import ListView, DetailView
# Define the home view function
# def home(request):
#     return HttpResponse('<h1>Hello to Rate My Device Website</h1>')

def home(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')


def device_index(request):
    devices = Device.objects.all()

    return render(request, 'devices/index.html', {'devices': devices})


class DeviceCreate(CreateView):
    model = Device
    fields = ['name', 'category', 'description', 'rate', 'warrenty_expration_Date', 'opinion']
