from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Device , User, Chat, Message, Reviews
from django.views.generic import CreateView, UpdateView,DeleteView
from django.views.generic import ListView, DetailView
from .forms import ReviewForm , DeviceUserCreationForm, DeviceForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

from django.db import models



# Define the home view function
class Home(LoginView):
    template_name = 'index.html'


def about(request):
    return render(request, 'about.html')

@login_required
def device_index(request):
    devices = Device.objects.all()

    return render(request, 'devices/index.html', {'devices': devices})


class DeviceCreate(LoginRequiredMixin, CreateView):
    model = Device
    form_class = DeviceForm

    def form_valid(self, form):
        print("form", form)
        form.instance.owner = self.request.user  
        return super().form_valid(form)

class DeviceUpdate(LoginRequiredMixin, UpdateView):
    model = Device
    form_class = DeviceForm

@login_required
def device_detail(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    reviews = device.reviews_set.all()
    review_form = ReviewForm()

    context = {
        'device': device,
        'review_form': review_form,
        'reviews': reviews,
        'owner_id': device.owner.id if device.owner else None  # Ensure owner_id is passed
    }

    return render(request, 'devices/detail.html', context)





# review
@login_required
def add_review(request, device_id):
    form = ReviewForm(request.POST)

    if form.is_valid():
        print(device_id)
        new_review = form.save(commit=False)
        new_review.devices_id = device_id
        new_review.user_id =1
        new_review.save()
    return redirect('device-detail', device_id=device_id)
    


class DeviceDelete(LoginRequiredMixin, DeleteView):
    model = Device
    success_url = '/devices/'

@login_required
def device_like(request, pk):
    device = get_object_or_404(Device, id=pk)

    if request.user in device.likes.all():
        device.likes.remove(request.user)  
    else:
        device.likes.add(request.user)  

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

    
    if request.user.id == user_id:
        return redirect('profile', username=request.user.username)
        
    existing_chat = Chat.objects.filter(
        (models.Q(sender=request.user) & models.Q(receiver=receiver)) |
        (models.Q(sender=receiver) & models.Q(receiver=request.user))
    ).first()
    
    if existing_chat:
        chat = existing_chat
    else:
        chat = Chat.objects.create(sender=request.user, receiver=receiver)
        

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




@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)

    devices = Device.objects.filter(owner=user)
    chats = Chat.objects.filter(sender=user) | Chat.objects.filter(receiver=user)
    
    chat_details = []
    processed_pairs = set()
    
    for chat in chats:
        pair_id = tuple(sorted([chat.sender.id, chat.receiver.id]))
        
        if pair_id not in processed_pairs:
            other_user = chat.receiver if chat.sender == user else chat.sender
            
            latest_chat = Chat.objects.filter(
                (models.Q(sender=pair_id[0]) & models.Q(receiver=pair_id[1])) |
                (models.Q(sender=pair_id[1]) & models.Q(receiver=pair_id[0]))
            ).latest('date_time')
            
            chat_details.append({
                'chat': latest_chat,
                'other_user': other_user
            })
            processed_pairs.add(pair_id)

    context = {
        'profile_user': user,
        'devices': devices,
        'chats': chat_details
    }
    
    return render(request, 'user/profile.html', context)

