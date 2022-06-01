from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "index.html")
