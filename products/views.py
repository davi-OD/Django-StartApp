from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# Create your views here.
def index(request):
    products = Product.object.all()
    return render(request, 'index.html', {'products': products})


def new_products(request):
    return HttpResponse('New Products')

