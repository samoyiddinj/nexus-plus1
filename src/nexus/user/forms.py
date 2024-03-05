from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control", "placeholder": "password1"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control", "placeholder": "retype password"
    }))

    class Meta:
        model = User
        fields = ('phone_number', 'username')
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control", "placeholder": "username"}),
            "phone_number": forms.TextInput(attrs={
                "class": "form-control", "placeholder": "+998901234567"
            })
        }


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control", "placeholder": "username"
            }),
            "password": forms.PasswordInput(attrs={
                "class": "form-control", "placeholder": "password"
            })
        }
