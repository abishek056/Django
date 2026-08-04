from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1> Hello my name is Abishek and I am a Django developer. Welcome to my blog! </h1>")

def about(request):
    return HttpResponse("<h1> This is the about page of my blog. Here you can learn more about me and my work. </h1>")
