from django.urls import path
from user import views

app_name = "user"

urlpatterns = [
    path("register/", views.register_request, name="register_request"),
    path("login/", views.login_request, name="login_request"),
    path("logout/", views.logout_request, name="logout_request"),
]
