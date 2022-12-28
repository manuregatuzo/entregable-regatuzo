from django.shortcuts import render
from django.http import HttpResponse

from products.models import Products, Category


# Create your views here.
def create_products(request):
    Products.objects.create(name='Sprite 500ml', price= 200, stock=True )
    return HttpResponse('Se creo el nuevo producto')


def list_products(request):
    all_products = Products.objects.all()
    context = {
        'products' : all_products,
    }
    return render(request, 'list_products.html', context=context)


def create_category(request):
    Category.objects.create(name = "Algo")    
    return HttpResponse("Se creo categoria")

def list_categories(request):
    all_categories = Category.objects.all()
    context = {
        'categories' : all_categories
    }
    return render(request, 'list_categories.html', context=context)
