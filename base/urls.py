from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

    path('', views.home, name="dashboard"),
    path('login/', views.loginPage, name="login"),
     path('login_account/', views.loginPage, name="login_account"),
    path('logout/', views.logoutPage, name="logout"),
    path('registration/', views.registrationPage, name="registration"),
    path('profile/', views.profileSetting, name="profile"),
#     path('admin_profile/', views.adminProfile, name="admin_profile"),

     path('restaurants/', views.restaurants, name="restaurants"),
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

    # feedbacks Management
    path('feedback/', views.feedback, name="feedback"),
    path('feedback_delete/<str:pk>/',
         views.deleteFeedback, name="feedback_delete"),

    # call_waiter Management
    path('call_waiter/', views.call_waiter, name="call_waiter"),
    path('callwaiter_delete/<str:pk>/',
         views.callWaiterDelete, name="callwaiter_delete"),


    path('qr_share/', views.qr_share, name="qr_share"),
    path('qr_generator/', views.qr_generator, name="qr_generator"),

    # restaurant Management
    path('restaurant/', views.restaurant, name="restaurant"),
    path('restaurant_create/', views.CreateRestaurant, name="restaurant_create"),
    path('restaurant_update/<str:pk>/',
         views.updateRestaurant, name="restaurant_update"),
    path('restaurant_delete/<str:pk>/',
         views.Restaurantdelete, name="restaurant_delete"),


    # staff Management
    path('staff/', views.staff, name="staff"),
    path('staff_create/', views.createStaff, name="staff_create"),
    path('staff_delete/<str:pk>/',
         views.deleteStaff, name="staff_delete"),

    # password Management
    path('reset_password/', auth_views.PasswordResetView.as_view(
         template_name="base/password/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name="base/password/password_reset_sent.html"
    ),
        name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="base/password/password_reset_form.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="base/password/password_reset_done.html"),
         name="password_reset_complete"),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name="base/password/password_change.html"),
         name="password_change"),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name="base/password/password_change_done.html"),
         name="password_change_done"),
]
