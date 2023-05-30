from django.urls import path
from . import views
app_name="user"

urlpatterns=[
    path("register/", views.register, name="register"),
    path("login/", views.login_request, name="login_request"),
    path("logout/", views.logout_request, name="logout_request")
]