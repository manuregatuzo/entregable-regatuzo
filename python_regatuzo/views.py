from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def hola_mundo(request):
    return HttpResponse("Hola mundo")

def otra_mas(request):
    return HttpResponse("Tu hermana")


def fecha_actual(request):
    hoy = datetime.now().date()
    return HttpResponse(f'La fecha de hoy es{hoy}')


def vista_con_edad(resquest, edad):
    return HttpResponse(f'Esto funcionma? la edad es {edad}')


def vista_con_template(request):
    return render(request, 'template.html', context={})

def saludo_desde_template(request):    
    context = {
        'nombre' : 'manuel', 
        'edad': 23,
        'lista_frutas' : ['manzana' , 'pera', 'banana']
    }
    return render(request, 'template.html', context=context )