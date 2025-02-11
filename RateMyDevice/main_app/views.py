from django.shortcuts import render
from django.http import HttpResponse
from .models import Device
from django.views.generic import CreateView, UpdateView,DeleteView
from django.views.generic import ListView, DetailView
# Define the home view function
def home(request):
    return HttpResponse('<h1>Hello to Rate My Device Website</h1>')


def about(request):
    return render(request, 'about.html')


def device_index(request):
    devices = Device.objects.all()

    return render(request, 'devices/index.html', {'devices': devices})


class DeviceCreate(CreateView):
    model = Device
    fields = ['name', 'category', 'description', 'rate', 'warrenty_expration_Date', 'opinion']
class DeviceCreate(CreateView):
    model = Device
    fields = ['name', 'category', 'description', 'rate', 'warrenty_expration_Date', 'opinion']

def device_detail(request, device_id):
    device = Device.objects.get(id=device_id)
    return render(request, 'devices/detail.html', {'device': device})
