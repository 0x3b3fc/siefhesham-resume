from django.shortcuts import render, get_object_or_404
from .models import Blog


# Create your views here.

def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog/index.html', {'blog': blog})


def detail(request, blog_id):
    post = get_object_or_404(Blog,pk=blog_id)
    all_blogs = Blog.objects.all()
    return render(request, 'blog/detail.html', {'post':post, 'blog':all_blogs})
