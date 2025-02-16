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
    warranty_expiration_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}) 
    )

    class Meta:
        model = Device
        fields = ['name', 'category', 'description', 'rate', 'warranty_expiration_date', 'opinion', 'image']

