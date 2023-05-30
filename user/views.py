from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate

def register(request):
    if request.method == "GET":
        return render(request, "user/register.html")
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["psw"]
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        
        try:
            User.objects.get(username=username)
            context = {"message": "User already exists"}
            return render(request, "user/register.html", context)
        except User.DoesNotExist:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password)
            login(request, user)
            context = {"message": "Registration successful"}
            redirect_url = reverse("quiz:main") + "?context=" + context["message"]
            return redirect(redirect_url)

def login_request(request):
    if request.method == "GET":
        return render(request, "user/login.html")
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["psw"]
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            context = {"message": "Login successful"}
            redirect_url = reverse("quiz:main") + "?context=" + context["message"]
            return redirect(redirect_url)
        else:
            context = {"message": "Invalid username or password"}
            return render(request, "user/login.html", context)

def logout_request(request):
    logout(request)
    context = {"message": "Logout successful"}
    redirect_url = reverse("quiz:main") + "?context=" + context["message"]
    return redirect(redirect_url)
