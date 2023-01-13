from django.shortcuts import render

from orders.models import Order
from orders.forms import OrderForm


def list_orders(request):
    orders = Order.objects.all()
    context = {
        'orders': orders
    }
    return render(request, 'list_orders.html', context=context)



def create_order(request):
    if request.method == 'GET':
        
        context = {
            'form' : OrderForm()
        }
        return render(request, 'create_order.html', context=context)

    elif request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            Order.objects.create(
                client=form.cleaned_data['client'],
                product=form.cleaned_data['product'],
                payment_method=form.cleaned_data['payment_method'],
            )

            context = {
                'message': 'Orden creado correctamente'
            }
            
        else:
            context = {
                'form_errors': form.errors,
                'form' : OrderForm()
            }
        return render(request, 'create_order.html', context=context)
