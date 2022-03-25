from itertools import product
from multiprocessing import context
from django.shortcuts import render
from apps.settings.models import Settings
from apps.products.models import Product
# Create your views here.

def index(request):
    home = Settings.objects.latest('id')
    product = Product.objects.all().order_by('-id')[:8]
    context = {
        'homes' : home,
        'products' : product,
    }
    return render(request, 'index-2.html', context)