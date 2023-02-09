
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from providers.models import Providers
from providers.forms import ProviderForm

def providers_list(request):
    
    providers = Providers.objects.filter(is_active = True)
    context = {
        'providers': providers
    }
    return render(request, 'providers/providers-list.html', context=context)


def providers_create(request):


    if request.method == 'GET':
        
        context = {
            'form' : ProviderForm()
        }
        return render(request, 'providers/providers-create.html', context=context)

    elif request.method == 'POST':
        form = ProviderForm(request.POST, request.FILES)
        if form.is_valid():
            Providers.objects.create(
                name= form.cleaned_data['name'],
                address= form.cleaned_data['address'],
                phone_number= form.cleaned_data['phone_number'],
                email = form.cleaned_data ['email'],
                condition = form.cleaned_data ['condition'],
                image=form.cleaned_data['image'],
            )

            context = {
                'message': 'Proveedor creado correctamente'
            }            
        else:
            context = {
                'form_errors': form.errors,
                'form' : ProviderForm()
            }
        return render(request, 'providers/providers-create.html', context=context)
    

def providers_update(request):
    provider_to_edit = request.GET['edit']
    provider = Providers.objects.filter(name=provider_to_edit)

    if request.method == 'GET':
        
        context = {
            'form' : ProviderForm(
            initial={
            'name':provider[0].name,            
            'adress':provider[0].address,
            'phone_number':provider[0].phone_number,
            'email':provider[0].email,
            'condition':provider[0].condition,            
            }
            
            )
        }
        return render(request, 'providers/providers-update.html', context=context)

    elif request.method == 'POST':
        form = ProviderForm(request.POST, request.FILES) 
        p = provider[0]       
        if form.is_valid():        
                p.name = form.cleaned_data['name']
                p.address = form.cleaned_data['address']
                p.phone_number = form.cleaned_data['phone_number']
                p.email = form.cleaned_data['email']
                p.condition = form.cleaned_data['condition']
                p.image=form.cleaned_data['image']               
                p.save()
                
        
                context = {
                'message': 'Proveedor actualizado correctamente'
            }            
        else:
            context = {
                'form_errors': form.errors,
                'form' : ProviderForm()
            }
        return render(request, 'providers/providers-update.html', context=context)
