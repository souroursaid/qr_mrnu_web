from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('category/', views.category, name="category"),
    path('category_create/', views.createCategory, name="category_create"),
    path('category_update/<str:pk>/', views.updateCategory, name="category_update"),
    path('category_delete/<str:pk>/', views.deleteCategory, name="category_delete"),

    #Tables Management
    path('table/', views.table, name="table"),
    path('table_create/', views.createTable, name="table_create"),
    path('table_update/<str:pk>/', views.updateTable, name="table_update"),
    path('table_delete/<str:pk>/', views.deleteTable, name="table_delete"),

    #Menu Management
    path('menu/', views.menu, name="menu"),
    path('menu_create/', views.createMenu, name="menu_create"),
    path('menu_update/<str:pk>/', views.updateMenu, name="menu_update"),
    path('menu_delete/<str:pk>/', views.deleteMenu, name="menu_delete"),

    path('order/', views.order, name="order"),
    path('order_create/', views.createOrder, name="order_create"),
    path('order_details/<str:pk>/', views.orderDetail, name="order_details"),
    path('order_update/<str:pk>/', views.updateOrder, name="order_update"),
    path('order_delete/<str:pk>/', views.deleteOrder, name="order_delete"),
]