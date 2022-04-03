from multiprocessing import context
from django.shortcuts import redirect, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib import messages
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from .models import *
from .forms import *

from django.conf import settings
from qrcode import *
import random

# Create your views here.


@unauthenticated_user
def registrationPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'base/registration.html', context)


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'base/login.html')


def logoutPage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    return render(request, 'base/home.html')


@login_required(login_url='login')
def profile(request):
    return render(request, 'base/profile.html')


@login_required(login_url='login')
def category(request):
    categorys = Category.objects.all()

    if 'q' in request.GET:
        q = request.GET['q']
        categorys = Category.objects.filter(name__icontains=q)

    item_count = categorys.count()

    page = request.GET.get('page', 1)
    paginator = Paginator(categorys, 4)
    try:
        categorys = paginator.page(page)
    except PageNotAnInteger:
        categorys = paginator.page(1)
    except EmptyPage:
        categorys = paginator.page(paginator.num_pages)

    context = {'categorys': categorys, 'item_count': item_count}
    return render(request, 'base/category.html', context)


@login_required(login_url='login')
def createCategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        # print('Pring POST', request.POST)
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your category was created successfully!', extra_tags='alert')
            return redirect('category')

    context = {'form': form}
    return render(request, 'base/forms/category_form.html', context)


@login_required(login_url='login')
def updateCategory(request, pk):
    category = Category.objects.get(id=pk)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        # print('Pring POST', request.POST)
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.info(
                request, 'Your category was updated successfully!', extra_tags='alert')
            return redirect('category')

    context = {'form': form}
    return render(request, 'base/forms/category_form.html', context)


@login_required(login_url='login')
def deleteCategory(request, pk):

    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        category.delete()
        messages.warning(
            request, 'Your category was deleted successfully!', extra_tags='alert')
        return redirect('category')

    context = {'item': category}
    return render(request, 'base/forms/delete_category.html', context)


@login_required(login_url='login')
def table(request):
    tables = Table.objects.all()

    if 'q' in request.GET:
        q = request.GET['q']
        tables = Table.objects.filter(table_Number__icontains=q)

    item_count = tables.count()

    page = request.GET.get('page', 1)
    paginator = Paginator(tables, 3)
    try:
        tables = paginator.page(page)
    except PageNotAnInteger:
        tables = paginator.page(1)
    except EmptyPage:
        tables = paginator.page(paginator.num_pages)

    context = {'tables': tables, 'item_count': item_count}
    return render(request, 'base/table.html', context)


@login_required(login_url='login')
def createTable(request):
    form = TableForm()
    if request.method == 'POST':
        # print('Pring POST', request.POST)
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your table was created successfully!', extra_tags='alert')
            return redirect('table')

    context = {'form': form}
    return render(request, 'base/forms/table_form.html', context)


@login_required(login_url='login')
def updateTable(request, pk):
    table = Table.objects.get(id=pk)
    form = TableForm(instance=table)
    if request.method == 'POST':
        # print('Pring POST', request.POST)
        form = TableForm(request.POST, instance=table)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your table was updated successfully!', extra_tags='alert')
            return redirect('table')

    context = {'form': form}
    return render(request, 'base/forms/table_form.html', context)


@login_required(login_url='login')
def deleteTable(request, pk):
    table = Table.objects.get(id=pk)
    if request.method == 'POST':
        table.delete()
        messages.success(
            request, 'Your table was deleted successfully!', extra_tags='alert')
        return redirect('table')

    context = {'item': table}
    return render(request, 'base/forms/delete_table.html', context)


@login_required(login_url='login')
def menu(request):
    menus = Menu.objects.all()

    if 'q' in request.GET:
        q = request.GET['q']
        menus = Menu.objects.filter(name__icontains=q)

    item_count = menus.count()

    page = request.GET.get('page', 1)
    paginator = Paginator(menus, 2)
    try:
        menus = paginator.page(page)
    except PageNotAnInteger:
        menus = paginator.page(1)
    except EmptyPage:
        menus = paginator.page(paginator.num_pages)

    context = {'menus': menus, 'item_count': item_count}
    return render(request, 'base/menu.html', context)


@login_required(login_url='login')
def createMenu(request):
    form = MenuForm()
    if request.method == 'POST':
        # print('Pring POST', request.POST)
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your menu item was created successfully!', extra_tags='alert')
            return redirect('menu')

    context = {'form': form}
    return render(request, 'base/forms/menu_form.html', context)


@login_required(login_url='login')
def updateMenu(request, pk):
    menu = Menu.objects.get(id=pk)
    form = MenuForm(instance=menu)
    if request.method == 'POST':
        # print('Pring POST', request.POST)
        form = MenuForm(request.POST, request.FILES, instance=menu)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your menu item was updated successfully!', extra_tags='alert')
            return redirect('menu')

    context = {'form': form}
    return render(request, 'base/forms/menu_form.html', context)


@login_required(login_url='login')
def deleteMenu(request, pk):
    menu = Menu.objects.get(id=pk)
    if request.method == 'POST':
        menu.delete()
        messages.success(
            request, 'Your menu item was deleted successfully!', extra_tags='alert')
        return redirect('menu')

    context = {'item': menu}
    return render(request, 'base/forms/delete_menu.html', context)


@login_required(login_url='login')
def order(request):
    orders = Order.objects.all()

    if 'q' in request.GET:
        q = request.GET['q']
        orders = Order.objects.filter(

            Q(place_order__icontains=q) |
            Q(customer__name__icontains=q) |
            Q(table__table_Number__icontains=q)
        )

    item_count = orders.count()

    page = request.GET.get('page', 1)
    paginator = Paginator(orders, 2)
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    context = {'orders': orders, 'item_count': item_count}
    return render(request, 'base/order.html', context)


@login_required(login_url='login')
def orderDetail(request, pk):
    order = Order.objects.get(id=pk)

    orderitems = order.orderitem_set.all()

    context = {'order': order, 'orderitems': orderitems}
    return render(request, 'base/order_details.html', context)


@login_required(login_url='login')
def createOrderItem(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderItemForm(initial={'order': order})
    if request.method == 'POST':
        # print('Pring POST', request.POST)
        form = OrderItemForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(
                request, 'Your order item was created successfully!', extra_tags='alert')
            return redirect('order_details', pk=order.pk)

    context = {'form': form}
    return render(request, 'base/forms/orderitem_from.html', context)


@login_required(login_url='login')
def updateOrderItem(request, pk):
    orderitem = OrderItem.objects.get(id=pk)
    form = OrderItemForm(instance=orderitem)
    if request.method == 'POST':
        # print('Pring POST', request.POST)
        form = OrderItemForm(request.POST, instance=orderitem)
        if form.is_valid():
            form.save()

            messages.success(
                request, 'Your order item was updated successfully!', extra_tags='alert')
            return redirect('order')

    context = {'form': form}
    return render(request, 'base/forms/orderitem_from.html', context)


@login_required(login_url='login')
def deleteOrderItem(request, pk):
    orderitem = OrderItem.objects.get(id=pk)
    if request.method == 'POST':
        orderitem.delete()
        messages.success(
            request, 'Your order item was deleted successfully!', extra_tags='alert')
        return redirect('order')

    context = {'item': orderitem}
    return render(request, 'base/forms/delete_order_item.html', context)


@login_required(login_url='login')
def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        # print('Pring POST', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your Order was created successfully!', extra_tags='alert')
            return redirect('order')

    context = {'form': form}
    return render(request, 'base/forms/order_form.html', context)


@login_required(login_url='login')
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        # print('Pring POST', request.POST)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your menu item was updated successfully!', extra_tags='alert')
            return redirect('order')

    context = {'form': form}
    return render(request, 'base/forms/order_form.html', context)


@login_required(login_url='login')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        messages.success(
            request, 'Your menu item was deleted successfully!', extra_tags='alert')
        return redirect('order')

    context = {'item': order}
    return render(request, 'base/forms/delete_order.html', context)


@login_required(login_url='login')
def reservation(request):
    reservations = Reservation.objects.all()

    if 'q' in request.GET:
        q = request.GET['q']
        reservations = Reservation.objects.filter(
            Q(table__table_Number__icontains=q) |
            Q(customer__name__icontains=q) |
            Q(date_visit__icontains=q)
        )

    item_count = reservations.count()

    page = request.GET.get('page', 1)
    paginator = Paginator(reservations, 3)
    try:
        reservations = paginator.page(page)
    except PageNotAnInteger:
        reservations = paginator.page(1)
    except EmptyPage:
        reservations = paginator.page(paginator.num_pages)

    context = {'reservations': reservations, 'item_count': item_count}
    return render(request, 'base/reservation.html', context)


@login_required(login_url='login')
def createReservation(request):
    form = ReservationForm()
    if request.method == 'POST':
        # print('Pring POST', request.POST)
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your reservation was created successfully!', extra_tags='alert')
            return redirect('reservation')

    context = {'form': form}
    return render(request, 'base/forms/reservation_form.html', context)


@login_required(login_url='login')
def updateReservation(request, pk):
    reservation = Reservation.objects.get(id=pk)
    form = ReservationForm(instance=reservation)
    if request.method == 'POST':
        # print('Pring POST', request.POST)
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your reservation was updated successfully!', extra_tags='alert')
            return redirect('reservation')

    context = {'form': form}
    return render(request, 'base/forms/reservation_form.html', context)


@login_required(login_url='login')
def deleteReservation(request, pk):
    reservation = Reservation.objects.get(id=pk)
    if request.method == 'POST':
        reservation.delete()
        messages.success(
            request, 'Your reservation was deleted successfully!', extra_tags='alert')
        return redirect('reservation')

    context = {'item': reservation}
    return render(request, 'base/forms/delete_reservation.html', context)


@login_required(login_url='login')
def deleteReservation(request, pk):
    reservation = Reservation.objects.get(id=pk)
    if request.method == 'POST':
        reservation.delete()
        messages.success(
            request, 'Your reservation was deleted successfully!', extra_tags='alert')
        return redirect('reservation')

    context = {'item': reservation}
    return render(request, 'base/forms/delete_reservation.html', context)


@login_required(login_url='login')
def feedback(request):
    feedbacks = Feedback.objects.all()

    if 'q' in request.GET:
        q = request.GET['q']
        feedbacks = Feedback.objects.filter(
            Q(username__icontains=q) |
            Q(email__icontains=q)
        )

    item_count = feedbacks.count()

    page = request.GET.get('page', 1)
    paginator = Paginator(feedbacks, 2)
    try:
        feedbacks = paginator.page(page)
    except PageNotAnInteger:
        feedbacks = paginator.page(1)
    except EmptyPage:
        feedbacks = paginator.page(paginator.num_pages)

    context = {'feedbacks': feedbacks, 'item_count': item_count}
    return render(request, 'base/feedback.html', context)


@login_required(login_url='login')
def deleteFeedback(request, pk):
    feedback = Feedback.objects.get(id=pk)
    if request.method == 'POST':
        feedback.delete()
        messages.success(
            request, 'Your table was deleted successfully!', extra_tags='alert')
        return redirect('feedback')

    context = {'item': feedback}
    return render(request, 'base/forms/delete_feedback.html', context)


@login_required(login_url='login')
def call_waiter(request):
    calls = Call_waiter.objects.all()
    context = {'calls': calls}
    return render(request, 'base/call_waiter.html', context)


def contact(request):
    contact = Contact_detail.objects.last()
    context = {'contact': contact}
    return render(request, 'base/contact_restaurant.html', context)


def CreateContact(request):
    form = ContactForm()
    if request.method == 'POST':
        # print('Pring POST', request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your reservation was created successfully!', extra_tags='alert')
            return redirect('contact')

    context = {'form': form}
    return render(request, 'base/forms/contact_form.html', context)


def contactdelete(request, pk):
    contact = Contact_detail.objects.get(id=pk)
    if request.method == 'POST':
        contact.delete()
        messages.success(
            request, 'Your table was deleted successfully!', extra_tags='alert')
        return redirect('contact')

    context = {'item': contact}
    return render(request, 'base/forms/delete_contact.html', context)


def updateContact(request, pk):
    contact = Contact_detail.objects.get(id=pk)
    form = ContactForm(instance=contact)
    if request.method == 'POST':
        # print('Pring POST', request.POST)
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your reservation was updated successfully!', extra_tags='alert')
            return redirect('contact')

    context = {'form': form}
    return render(request, 'base/forms/contact_form.html', context)


@login_required(login_url='login')
def qr_generator(request):
    if request.method == "POST":
        Url = request.POST['url']
        QrCode.objects.create(url=Url)

    qr_code = QrCode.objects.all()
    return render(request, "base/qr_generator.html", {'qr_code': qr_code})


@login_required(login_url='login')
def qr_share(request):
    qr_code = QrCode.objects.last()
    context = {'qr_code': qr_code}
    return render(request, 'base/qr_share.html', context)


def callWaiterDelete(request, pk):
    call = Call_waiter.objects.get(id=pk)
    if request.method == 'POST':
        call.delete()
        messages.success(
            request, 'Your table was deleted successfully!', extra_tags='alert')
        return redirect('call_waiter')

    context = {'item': call}
    return render(request, 'base/forms/delete_call.html', context)
