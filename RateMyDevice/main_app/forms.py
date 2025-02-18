from django import forms
from .models import Reviews , Device
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['comments']
        widgets = {
            'comments': forms.Textarea()
        }
        ordering = ['-comment']

class DeviceUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class DeviceForm(forms.ModelForm):
    warrenty_expration_Date = forms.DateField(
        widget=forms.DateInput(format="%Y-%m-%d", attrs={'type': 'date'}))
    rate = forms.FloatField(
        widget=forms.NumberInput(attrs={'min': 0, 'max': 5, 'step': 0.1}) 
    )

    class Meta:
        model = Device
        fields = ['name', 'category', 'description', 'rate', 'warrenty_expration_Date', 'opinion', 'image']

