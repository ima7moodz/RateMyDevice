from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Device , User, Chat, Message
from django.views.generic import CreateView, UpdateView,DeleteView
from django.views.generic import ListView, DetailView
from .forms import ReviewForm , DeviceUserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

# Define the home view function
class Home(LoginView):
    template_name = 'index.html'


def about(request):
    return render(request, 'about.html')


def device_index(request):
    devices = Device.objects.all()

    return render(request, 'devices/index.html', {'devices': devices})


class DeviceCreate(LoginRequiredMixin, CreateView):
    model = Device
    fields = ['name', 'category', 'description', 'rate', 'warrenty_expration_Date', 'opinion']

    def form_valid(self, form):
        form.instance.owner = self.request.user  
        return super().form_valid(form)

def device_detail(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    reviews = device.reviews_set.all()
    review_form = ReviewForm()

    context = {
        'device': device,
        'review_form': review_form,
        'reviews': reviews
    }
    
    if device.owner:  
        context['owner_id'] = device.owner.id  

    return render(request, 'devices/detail.html', context)




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



def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = DeviceUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email'] 
            user.save()
            login(request, user)
            return redirect('device-ind')
        else:
            error_message = 'Invalid signup - Please try again later.'

    form = DeviceUserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

@login_required
def start_chat(request, user_id):
    receiver = get_object_or_404(User, id=user_id)
    chat, created = Chat.objects.get_or_create(sender=request.user, receiver=receiver)
    return redirect('chat-room', chat_id=chat.id)


@login_required
def chat_room(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    
    if request.method == "POST":
        message_content = request.POST.get('message')
        if message_content:
            Message.objects.create(chat=chat, sender=request.user, content=message_content)
    
    messages = chat.messages.all().order_by("timestamp")
    return render(request, 'chats/chat_room.html', {'chat': chat, 'messages': messages})