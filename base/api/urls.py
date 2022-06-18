from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes, name="api_routes"),
    path('categorys/', views.getCategorys, name="categorys_api"),
    path('categorys/<str:pk>', views.getCategory, name="category_api"),
    path('categorys_create/', views.createCategory, name="categorys_create"),
    path('categorys_update/<str:pk>/',
         views.updateCategory, name="categorys_update_api"),
    path('category_delete/<str:pk>/',
         views.deleteCategory, name="category_delete_api"),

    path('restaurants/', views.getRestaurants, name="restaurants_api"),
    path('restaurant/<str:pk>', views.getRestaurant, name="restaurant_api"),

    path('menus/', views.getMenus, name="menus_api"),
    path('menus/<str:pk>', views.getMenu, name="menu_api"),

    path('tables/', views.getTables, name="tables_api"),
    path('tables/<str:pk>', views.getTable, name="table_api"),

    path('call_waiter/', views.getCalls, name="call_waiters_api"),
    path('call_waiter_create/', views.createCall, name="call_waiter_create_api"),

    path('feedbacks/', views.getFeedbacks, name="feedbacks_api"),
    path('feedback_create/', views.createFeedback, name="feedback_create_api"),

    path('reservations/', views.getReservations, name="feedbacks_api"),
    path('reservation_create/', views.createReservation,
         name="reservation_create_api"),

    path('order_items/', views.getOrderItem, name="order_items_api"),


    path('orderitem_create/', views.createOrderItem, name="orderitem_create_api"),


]
