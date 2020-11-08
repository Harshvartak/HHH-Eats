from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from . import views


# app_name="foodapp"
urlpatterns = [
    path("",views.home,name="home"),
    path("login/",views.login_view,name="login"),

    path("customer/register",views.customerRegister,name="customer_register"),
    path("customer/home",views.index,name="customer_home"),

    # path("owner/register",views.RestaurantRegister,name="restaurant_register"),
    # path("owner/home",views.rest_index,name="restaurant_home"),

    path("showMenu/",views.listRestaurant,name="ListRestaurant"),
    path("menu/<int:pk>",views.restuarantMenu,name="restuarantMenu"),

    path("neworder/<int:pk>/<int:rid>",views.new_order,name="NewOrder"),
    path("removeorder/<int:pk>/<int:rid>",views.remove_order,name="remove order"),

    path("neworder_cart/<int:pk>/<int:rid>",views.new_order_cart,name="NewOrderCart"),
    path("removeorder_cart/<int:pk>/<int:rid>",views.remove_order_cart,name="RemoveOrderCart"),
    path("customer/cart/<int:rid>",views.view_cart,name="cart"),

    path("customer/cart/checkout/<int:rid>",views.checkout,name="checkout"),
    path("customer/orders",views.order_status,name="order_status")
]
