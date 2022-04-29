from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return  render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def info(request):
    return render(request, 'info.html')

def course(request):
    return render(request, 'course.html')

def map(request):
    return render(request, 'map.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def user(request):
    return render(request, 'user.html')

