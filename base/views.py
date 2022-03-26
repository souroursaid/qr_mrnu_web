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

    context = {'orders': orders, 'orderitems': orderitems}
    return render(request, 'base/order_details.html', context)


def createOrderItem(request, pk):
    order = Order.objects.get(id=pk)
    OrderFormSet = inlineformset_factory(
        Order, OrderItem, fields=('menu', 'quantity'), extra=2)

    formset = OrderFormSet(instance=order)
    if request.method == 'POST':
        print('Pring POST', request.POST)
        formset = OrderItemForm(request.POST, instance=order)
        if formset.is_valid():
            formset.save()
            return redirect('order_details', pk=order.pk)

    context = {'formset': formset}
    return render(request, 'base/forms/orderitem_from.html', context)


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
        form = OrderForm(request.POST, instance=order)
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


def reservation(request):

    reservations = Reservation.objects.all()
    context = {'reservations': reservations}
    return render(request, 'base/reservation.html', context)


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


def deleteReservation(request, pk):
    reservation = Reservation.objects.get(id=pk)
    if request.method == 'POST':
        reservation.delete()
        messages.success(
            request, 'Your reservation was deleted successfully!', extra_tags='alert')
        return redirect('reservation')

    context = {'item': reservation}
    return render(request, 'base/forms/delete_reservation.html', context)


def deleteReservation(request, pk):
    reservation = Reservation.objects.get(id=pk)
    if request.method == 'POST':
        reservation.delete()
        messages.success(
            request, 'Your reservation was deleted successfully!', extra_tags='alert')
        return redirect('reservation')

    context = {'item': reservation}
    return render(request, 'base/forms/delete_reservation.html', context)


def feedback(request):
    feedbacks = Feedback.objects.all()

    context = {'feedbacks': feedbacks}
    return render(request, 'base/feedback.html', context)


def deleteFeedback(request, pk):
    feedback = Feedback.objects.get(id=pk)
    if request.method == 'POST':
        feedback.delete()
        messages.success(
            request, 'Your table was deleted successfully!', extra_tags='alert')
        return redirect('feedback')

    context = {'item': feedback}
    return render(request, 'base/forms/delete_feedback.html', context)


def call_waiter(request):
    calls = Call_waiter.objects.all()
    context = {'calls': calls}
    return render(request, 'base/call_waiter.html', context)


def qr_share(request):
    return render(request, 'base/qr_share.html')
