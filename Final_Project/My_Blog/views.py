from pydoc_data.topics import topics
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic, Article

# Create your views here.
def show_titles(request):
    titles = Article.objects.all()
    return render(request, 'My_Blog/project.html', {'title':titles})

def homepage(request):
    return render(request,'My_Blog/home.html')

def projects(request):
    return render(request, 'My_Blog/project.html')

def vision(request):
    return render(request, 'My_Blog/vision.html')

def contact(request):
    return render(request, 'My_Blog/contact.html')
