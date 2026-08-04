from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.

# def index(request):
#     # return HttpResponse("<h1> Hello my name is Abishek and I am a Django developer. Welcome to my blog! </h1>")
#     return render(request, 'blog/home.html')


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def post_detail(request, slug):
    # post = Post.objects.get(slug=slug)
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})


def about(request):
    return HttpResponse("<h1> This is the about page of my blog. Here you can learn more about me and my work. </h1>")
