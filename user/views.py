from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
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
            context = {"message": "User already exists"}
            return render(request, "user/register.html", context)
        except User.DoesNotExist:
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password,
            )
            login(request, user)
            logger.debug(f"Register user: {username}")
            context = {"message": "Registration successful"}
            return render(request, "quiz/menu_main.html", context=context)

    return render(request, "user/register.html", context=context)


def login_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["psw"]
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            logger.debug(f"Login user: {username} ")
            context = {"message": "Login successful"}
            return render(request, "quiz/menu_main.html", context=context)

        else:
            context = {"message": "Invalid username or password"}
    return render(request, "user/login.html")


def logout_request(request):
    logger.debug(f"Logout user: {request.user.username}")
    logout(request)
    context = {"message": "Logout successful"}
    return render(request, "quiz/menu_main.html", context=context)
