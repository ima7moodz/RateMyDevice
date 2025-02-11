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

class DeviceCreate(CreateView):
    model = Device
    fields = ['name', 'category', 'description', 'rate', 'warrenty_expration_Date', 'opinion']
def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {'cat': cat})