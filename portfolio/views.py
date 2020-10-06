from django.shortcuts import render
from .models import Project


def home(request):
    projects=Project.objects.all()
    return render(request,'portfolio/home.html',{'projects':projects})

def about(request):
    return render(request,'portfolio/about.html')

def store(request):
    return render(request,'portfolio/store.html')

def sample(request):
    return render(request,'portfolio/sample.html')
