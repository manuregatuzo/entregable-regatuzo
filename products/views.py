from django.shortcuts import render

from products.models import Products
from products.forms import ProductForm



def create_products(request):
    if request.method == 'GET':
        
        context = {
            'form' : ProductForm()
        }
        return render(request, 'products/create_product.html', context=context)

    elif request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            Products.objects.create(
                name=form.cleaned_data['name'],
                price=form.cleaned_data['price'],
                stock=form.cleaned_data['stock'],
                image=form.cleaned_data['image'],
            )

            context = {
                'message': 'Producto creado correctamente'
            }
            return render(request, 'products/create_product.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form' : ProductForm()
            }
            return render(request, 'products/create_product.html', context=context)


def list_products(request):
    if 'search' in request.GET:        
        search = request.GET['search']
        products = Products.objects.filter (name__contains=search)
    elif 'delete' in request.GET:   
        delete = request.GET['delete']        
        Products.objects.filter(name=delete).delete() 
        products = Products.objects.all()
    else:        
        products = Products.objects.all()
    context = {
        'products' : products,
    }
    return render(request, 'products/list_products.html', context=context)


