
from django.shortcuts import render
from django.db.models import Q
from base.models import Menu, Category

# Create your views here.


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    menus = Menu.objects.filter(
        Q(category__name__icontains=q) | 
        Q(name__icontains=q) |
        Q(description__icontains=q)|
        Q(price__icontains=q)
    )

    categorys = Category.objects.all()

    context = {'menus': menus,'categorys':categorys}
    return render(request, 'frontend_menu/home.html', context)

def menuDetails(request,pk):
    menu = Menu.objects.get(id=pk)
    context = {'menu':menu}
    return render(request, 'frontend_menu/menu_details.html',context)

