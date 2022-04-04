from django.urls import path, re_path, include
from . import views


urlpatterns = [

    path('', views.home, name="dashboard"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('registration/', views.registrationPage, name="registration"),
    path('profile/', views.profile, name="profile"),

    # Categories Management
    path('category/', views.category, name="category"),
    path('category_create/', views.createCategory, name="category_create"),
    path('category_update/<str:pk>/',
         views.updateCategory, name="category_update"),
    path('category_delete/<str:pk>/',
         views.deleteCategory, name="category_delete"),

    # Tables Management
    path('table/', views.table, name="table"),
    path('table_create/', views.createTable, name="table_create"),
    path('table_update/<str:pk>/', views.updateTable, name="table_update"),
    path('table_delete/<str:pk>/', views.deleteTable, name="table_delete"),

    # Menu Management
    path('menu/', views.menu, name="menu"),
    path('menu_create/', views.createMenu, name="menu_create"),
    path('menu_update/<str:pk>/', views.updateMenu, name="menu_update"),
    path('menu_delete/<str:pk>/', views.deleteMenu, name="menu_delete"),

    # Order Management
    path('order/', views.order, name="order"),
    path('order_create/', views.createOrder, name="order_create"),
    path('order_details/<str:pk>/', views.orderDetail, name="order_details"),
    path('order_update/<str:pk>/', views.updateOrder, name="order_update"),
    path('order_delete/<str:pk>/', views.deleteOrder, name="order_delete"),

    path('order_item_create/<str:pk>/',
         views.createOrderItem, name="order_item_create"),
    path('order_item_update/<str:pk>/',
         views.updateOrderItem, name="order_item_update"),
     path('order_item_delete/<str:pk>/',
         views.deleteOrderItem, name="order_item_delete"),


    # Reservations Management
    path('reservation/', views.reservation, name="reservation"),
    path('reservation_create/', views.createReservation, name="reservation_create"),
    path('reservation_update/<str:pk>/',
         views.updateReservation, name="reservation_update"),
    path('reservation_delete/<str:pk>/',
         views.deleteReservation, name="reservation_delete"),

    path('feedback/', views.feedback, name="feedback"),
    path('feedback_delete/<str:pk>/',
         views.deleteFeedback, name="feedback_delete"),

    path('call_waiter/', views.call_waiter, name="call_waiter"),
    path('qr_share/', views.qr_share, name="qr_share"),
    path('qr_generator/', views.qr_generator, name="qr_generator"),

    path('restaurant/', views.restaurant, name="restaurant"),
    path('restaurant_create/', views.CreateRestaurant, name="restaurant_create"),
    path('restaurant_update/<str:pk>/', views.updateRestaurant, name="restaurant_update"),
    path('restaurant_delete/<str:pk>/', views.Restaurantdelete, name="restaurant_delete"),

    path('callwaiter_delete/<str:pk>/', views.callWaiterDelete, name="callwaiter_delete"),
    

    

]
