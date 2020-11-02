from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from . import views

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html", authentication_form=LoginForm
        ),
        name="login",
    ),
    path("register/",views.register,name="register")
]
