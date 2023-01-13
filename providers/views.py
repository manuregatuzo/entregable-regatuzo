from django.shortcuts import render

from providers.models import Providers
from providers.forms import ProviderForm

def providers_list(request):
    
    providers = Providers.objects.filter(is_active = True)
    context = {
        'providers': providers
    }
    return render(request, 'providers-list.html', context=context)


def providers_create(request):

    if request.method == 'GET':
        
        context = {
            'form' : ProviderForm()
        }
        return render(request, 'providers-create.html', context=context)

    elif request.method == 'POST':
        form = ProviderForm(request.POST)
        if form.is_valid():
            Providers.objects.create(
                name= form.cleaned_data['name'],
                address= form.cleaned_data['address'],
                phone_number= form.cleaned_data['phone_number'],
                email = form.cleaned_data ['email'],
                condition = form.cleaned_data ['condition'],
            )

            context = {
                'message': 'Proveedor creado correctamente'
            }            
        else:
            context = {
                'form_errors': form.errors,
                'form' : ProviderForm()
            }
        return render(request, 'providers-create.html', context=context)