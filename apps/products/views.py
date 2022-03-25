from itertools import product
from turtle import home
from django.shortcuts import render
from apps.products.models import Product
from apps.settings.models import Settings

# Create your views here.

def product_detail(request, id):
    product = Product.objects.get(id = id)
    home = Settings.objects.latest('id')
    context ={
        'product': product,
        'home' : home,
    }
    return render(request, 'product-left-sedebar.html', context)