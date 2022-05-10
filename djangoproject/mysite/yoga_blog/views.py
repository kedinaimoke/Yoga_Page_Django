from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'yoga_blog/index.html', {'posts': posts})


def home(request):
    return render(request, 'yoga_blog/index.html', {})


def blog(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'yoga_blog/blog.html', {'post': post})


def contact(request):
    return render(request, 'yoga_blog/contact.html', {})
