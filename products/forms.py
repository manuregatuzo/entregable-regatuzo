from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nombre')
    price = forms.FloatField(label='Precio')
    stock = forms.BooleanField(required=False)
    image = forms.ImageField(required=False, label='Imagen')