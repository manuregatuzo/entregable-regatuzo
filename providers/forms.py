from django import forms


CONDITION_CHOICES = (
        ('monotributista', 'monotribustista'),
        ('responsable inscripto','responsable inscripto'),
        )

class ProviderForm(forms.Form):
        name = forms.CharField(max_length=100, label='Nombre')
        address = forms.CharField(max_length=300, label='Direccion')
        phone_number = forms.CharField(max_length=20, label='Numero de telefono')
        email = forms.EmailField()
        condition = forms.ChoiceField(choices = CONDITION_CHOICES, label='Conidicion')
        image = forms.ImageField(required=False, label='Imagen')
