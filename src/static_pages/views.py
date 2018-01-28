from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.

def index(request):
    return HttpResponse("Hello World")