from django.shortcuts import render
from core.erp.models import Category, Product


# Create your views here.

def myfirstview(request):
    categories = Category.objects.all()

    return render(request, 'index.html', {'categories': categories})

def secondview(request):
    data = {
            'name' : 'Jorge',
            'products' : Product.objects.all()

            }
    return render(request, 'second.html', data)
