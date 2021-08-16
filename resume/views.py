from django.shortcuts import render
from .models import Project
from blog.models import Blog
# Create your views here.

def home(request):
    projects = Project.objects.all()
    blogs = Blog.objects.all()
    return render(request, 'resume/index.html', {'projects':projects, 'blogs':blogs})