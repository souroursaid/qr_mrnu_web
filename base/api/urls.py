from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes, name="api_routes"),
    path('categorys/', views.getCategorys, name="categorys"),
    path('categorys/<str:pk>', views.getCategory, name="category"),
    path('categorys_create/', views.createCategory, name="categorys_create"),
    path('categorys_update/<str:pk>/',
         views.updateCategory, name="categorys_update"),
    path('category_delete/<str:pk>/',
         views.deleteCategory, name="category_delete"),

    path('restaurants/', views.getRestaurants, name="restaurants"),
    path('restaurant/<str:pk>', views.getRestaurant, name="restaurant"),

    path('menus/', views.getMenus, name="menus"),
    path('menus/<str:pk>', views.getMenu, name="menu"),

    path('tables/', views.getTables, name="tables"),
    path('tables/<str:pk>', views.getTable, name="table"),

    path('call_waiter/', views.getCalls, name="call_waiters"),
    path('call_waiter_create/', views.createCall, name="call_waiter_create"),

    path('feedbacks/', views.getFeedbacks, name="feedbacks"),
    path('feedback_create/', views.createFeedback, name="feedback_create"),

    path('reservations/', views.getReservations, name="feedbacks"),
    path('reservation_create/', views.createReservation, name="reservation_create"),

    path('order_items/', views.getOrderItems, name="order_items"),
    path('order_item_create/', views.createOrderItem, name="order_item_create"),

    path('orders/', views.getOrders, name="orders"),
    path('orders/<str:pk>', views.getOrder, name="order"),
    path('orders_create/', views.createOrder, name="orders_create"),
    path('orders_update/<str:pk>/',
         views.updateOrder, name="orders_update"),

]
