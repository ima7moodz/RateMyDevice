from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Device
from django.views.generic import CreateView, UpdateView,DeleteView
from django.views.generic import ListView, DetailView
from .forms import ReviewForm
# Define the home view function
def home(request):
    devices = Device.objects.all()
    
    return render(request, 'devices/index.html', {'devices': devices})


def about(request):
    return render(request, 'about.html')


def device_index(request):
    devices = Device.objects.all()

    return render(request, 'devices/index.html', {'devices': devices})


class DeviceCreate(CreateView):
    model = Device
    fields = ['name', 'category', 'description', 'rate', 'warrenty_expration_Date', 'opinion']

def device_detail(request, device_id):
    device = Device.objects.get(id=device_id)
    reviews = device.reviews_set.all()
    review_form = ReviewForm()

    return render(request, 'devices/detail.html', {'device': device, 
                                                'review_form': review_form,
                                                'reviews': reviews})



# review
def add_review(request, device_id):
    form = ReviewForm(request.POST)

    if form.is_valid():
        print(device_id)
        new_review = form.save(commit=False)
        new_review.devices_id = device_id
        new_review.user_id =1
        new_review.save()
    return redirect('device-detail', device_id=device_id)
    return render(request, 'devices/detail.html', {'device': device})

class DeviceUpdate(UpdateView):
    model = Device
    fields = ['name', 'category', 'description', 'rate', 'warrenty_expration_Date', 'opinion']

class DeviceDelete(DeleteView):
    model = Device
    success_url = '/devices/'

def device_like(request, pk):
    device = get_object_or_404(Device, id=pk)
    device.likes += 1 
    device.save()
    return redirect('device-detail', device_id=pk)




