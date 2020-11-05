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
    path("register/",views.register,name="register"),
    path("customer/register",views.customerRegister,name="customer_register"),
    path("customer/home",views.index,name="customer_home"),
    path("owner/register",views.RestaurantRegister,name="restaurant_register"),
    path("owner/home",views.rest_index,name="restaurant_home"),
    path("showMenu/",views.listRestaurant,name="ListRestaurant"),
    path("menu/<int:pk>",views.restuarantMenu,name="restuarantMenu"),
    # path("test/",views.testing,name="test")
]
