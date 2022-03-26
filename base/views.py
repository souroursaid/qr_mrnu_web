from django.shortcuts import redirect, render
from django.contrib import messages
from django.forms import inlineformset_factory
from .models import *
from .forms import *
# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def category(request):
    categorys = Category.objects.all()
    context = {'categorys': categorys}
    return render(request, 'base/category.html', context)

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

def deleteCategory(request, pk):

    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        category.delete()
        messages.warning(
            request, 'Your category was deleted successfully!', extra_tags='alert')
        return redirect('category')

    context = {'item': category}
    return render(request, 'base/forms/delete_category.html', context)

def table(request):
    tables = Table.objects.all()

    context = {'tables': tables}
    return render(request, 'base/table.html', context)



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


def deleteTable(request, pk):
    table = Table.objects.get(id=pk)
    if request.method == 'POST':
        table.delete()
        messages.success(
            request, 'Your table was deleted successfully!', extra_tags='alert')
        return redirect('table')

    context = {'item': table}
    return render(request, 'base/forms/delete_table.html', context)

def menu(request):
    menus = Menu.objects.all()


    context = {'menus': menus}
    return render(request, 'base/menu.html', context)



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



def deleteMenu(request, pk):
    menu = Menu.objects.get(id=pk)
    if request.method == 'POST':
        menu.delete()
        messages.success(
            request, 'Your menu item was deleted successfully!', extra_tags='alert')
        return redirect('menu')

    context = {'item': menu}
    return render(request, 'base/forms/delete_menu.html', context)

def order(request):
    orders = Order.objects.all()


    context = {'orders': orders}
    return render(request, 'base/order.html', context)

def orderDetail(request, pk):
    orders = Order.objects.filter(id=pk)
    orderitems = OrderItem.objects.filter(order_id=pk)
    orderdelivery = Order.objects.filter(place_order='Delivery')
    orderrestaurant = Order.objects.filter(place_order='Restaurant')
    


    context = {'orders': orders,'orderitems':orderitems,'orderdelivery':orderdelivery,'orderrestaurant':orderrestaurant}
    return render(request, 'base/order_details.html', context)

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

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        # print('Pring POST', request.POST)
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your menu item was updated successfully!', extra_tags='alert')
            return redirect('order')

    context = {'form': form}
    return render(request, 'base/forms/order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        messages.success(
            request, 'Your menu item was deleted successfully!', extra_tags='alert')
        return redirect('order')

    context = {'item': order}
    return render(request, 'base/forms/delete_order.html', context)
