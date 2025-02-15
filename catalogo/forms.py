from django.core.exceptions import ValidationError
from django import forms
from .models import DVD
from .models import VHS
from .models import VideoEquipments
from .models import Client
from .models import Purchase
from .models import Product

class DVDForm(forms.ModelForm):
    class Meta:
        model = DVD
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'year': 'año',
            'genre': 'Género',
            'description': 'Descripción',
            'price': 'Precio',
            'picture': 'Foto',
            'category': 'categoría',
            }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.DateInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

class VHSForm(forms.ModelForm):
    class Meta:
        model = VHS
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'year': 'año',
            'type': 'Tipo',
            'description': 'Descripción',
            'price': 'Precio',
            'picture': 'Foto',
            'category': 'categoría',
            }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.DateInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

class VideoEquipmentsForm(forms.ModelForm):
    class Meta:
        model = VideoEquipments
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'year': 'año',
            'description': 'Descripción',
            'price': 'Precio',
            'picture': 'Foto',
            'category': 'categoría',
            }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.DateInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

class PurchaseForm(forms.ModelForm):
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )
    total_price = forms.DecimalField(widget=forms.HiddenInput(), required=True)

    class Meta:
        model = Purchase
        fields = ['client', 'products', 'total_price']
        labels = {
            'client': 'Cliente',
        }
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
        }


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'email': 'Correo',
            'phone': 'Teléfono',
            'adress': 'Dirección',
            'payment': 'Método de pago',
            }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'adress': forms.TextInput(attrs={'class': 'form-control'}),
            'payment': forms.Select(attrs={'class': 'form-control'}),
        }