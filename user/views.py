from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    return

def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    return

def logout(request):
    return