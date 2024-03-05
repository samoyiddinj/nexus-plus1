from django import forms
from .models import Product
from django.contrib.auth.forms import UserCreationForm

from nexus.product.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title",  'description', 'city', 'price', 'category', 'state', ]
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control input-md ', 'placeholder': 'Title'}),
            "category": forms.Select(attrs={'class': 'tg-select form-control'}),
            "description": forms.Textarea(attrs={'class': 'w-full py-4 px-4 rounded-xl border'})
        }
