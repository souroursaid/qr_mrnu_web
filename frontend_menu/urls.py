from django.urls import path, re_path, include
from . import views


urlpatterns = [

    path('home/', views.home, name="home"),

    ]