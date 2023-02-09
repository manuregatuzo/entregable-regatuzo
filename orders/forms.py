from django import forms

CONDITION_CHOICES = (
        ('efectivo', 'efectivo'),
        ('tarjeta de credito','tarjeta de credito'),
        )


class OrderForm(forms.Form):
    client = forms.CharField(max_length=100, label= 'Cliente')
    product = forms.CharField(max_length=100, label = 'Producto')    
    payment_method = forms.ChoiceField(choices = CONDITION_CHOICES, label= 'Metodo de pago')