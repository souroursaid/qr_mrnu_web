from django.urls import path, re_path, include
from . import views


urlpatterns = [

    path('', views.home, name="home"),
    path('menu_details/<str:pk>/', views.menuDetails, name="menu_details"),
    path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    ]