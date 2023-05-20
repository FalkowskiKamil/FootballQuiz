from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
import logging
logger = logging.getLogger(__name__)

# Create your views here.
def register(request):
    context={}
    if request.method == 'GET':
        return render(request, 'user/register.html', context)
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist=True
        except:
            logger.error("New user")
        if not user_exist:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password)
            login(request, user)      
            context['message'] = 'Register Succesfully'
            redirect_url = reverse('quiz:main') + '?context=' + context['message']
            return redirect(redirect_url)
        else:
            context['message']='User alredy exist.'
            return render(request, 'user/register.html', context)
        
    return

def login_request(request):
    context={}
    if request.method == 'GET':
        return render(request, 'user/login.html', context)
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            context['message'] = 'Login Succesfully'
            redirect_url = reverse('quiz:main') + '?context=' + context['message']
            return redirect(redirect_url)
        else:
            context['message'] = 'Invalid username or password'
            return render(request, 'user/login.html', context)

def logout_request(request):
    context={}
    logout(request)
    context['message'] = 'Logout succesfully'
    redirect_url = reverse('quiz:main') + '?context=' + context['message']
    return redirect(redirect_url)