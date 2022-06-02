
from django.shortcuts import render, redirect
from django.db.models import Q
from base.models import *
from cart.cart import Cart
# Create your views here.


def home(request):
    return render(request, 'frontend_menu/qrhome.html')

