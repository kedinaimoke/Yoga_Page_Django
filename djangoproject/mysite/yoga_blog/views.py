from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.


def blog(request):
    posts = Post.objects.all()
    return render(request, 'yoga_blog/blog.html', {'posts': posts})


def singlepost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'yoga_blog/singlepost.html', {'post': post})
