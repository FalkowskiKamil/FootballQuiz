from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from utils.logger import configure_logger

logger = configure_logger()


def register_request(request):
    context = {}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["psw"]
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        try:
            User.objects.get(username=username)
            messages.error(request, "User already exists")
            return redirect(reverse("user:register_request"))
        except User.DoesNotExist:
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password,
            )
            login(request, user)
            logger.debug(f"Register user: {username}")
            messages.success(request, "Successfully registered!")
            return redirect(reverse("football_quiz:main"))
    return render(request, "user/register.html", context=context)


def login_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["psw"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            logger.debug(f"Login user: {username} ")
            messages.success(request, "Successfully logged in!")
            return redirect(reverse("football_quiz:main"))
        else:
            messages.error(request, "Invalid username or password")
            return redirect(reverse, "football_quiz:main")
    return render(request, "user/login.html")


def logout_request(request):
    logger.debug(f"Logout user: {request.user.username}")
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect(reverse("football_quiz:main"))
