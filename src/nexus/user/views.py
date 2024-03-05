from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login


def my_login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = login(username, password)

            if user is not None:
                authenticate(username, password)

    ctx = {
        'form': form
    }
    return render(request, 'login.html', ctx)


def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        print(form, form.is_valid())
        if form.is_valid:
            form.save()
            return redirect("login")

    ctx = {
        'form': form
    }
    return render(request, 'register.html', ctx)
