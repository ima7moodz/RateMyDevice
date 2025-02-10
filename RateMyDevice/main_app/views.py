from django.shortcuts import render
from django.http import HttpResponse

# Define the home view function
def home(request):
    return HttpResponse('<h1>Hello to Rate My Device Website</h1>')


def about(request):
    return render(request, 'about.html')