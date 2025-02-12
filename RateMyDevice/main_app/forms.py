from django import forms
from .models import Reviews


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['comments']
        widgets = {
            'comments': forms.Textarea()
        }
        ordering = ['-comment']