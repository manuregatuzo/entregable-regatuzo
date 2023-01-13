from django import forms

class OrderForm(forms.Form):
    client = forms.CharField(max_length=100)
    product = forms.CharField(max_length=100)    
    payment_method = forms.CharField( max_length=4)