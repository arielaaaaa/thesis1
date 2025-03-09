from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

# Create your views here.

def home(request):
    name = profile.objects.all()
    return render(request, 'myapp/home.html', {'name': name})


def about(request):
    return render(request, 'myapp/about.html')

def services(request):
    return render(request, 'myapp/services.html')

def contact(request):
    return render(request, 'myapp/contact.html')

def assesment(request):
    return render(request, 'myapp/assesment.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:  # Catch duplicate username error
                form.add_error('username',
                'This username is already taken. Please choose another one.')
    else:
        form = CustomUserCreationForm()
    return render(request,
    'myapp/register.html',
    {'form': form}
    )

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request,
    'myapp/login.html',
    {'form': form}
    )

def user_logout(request):
    logout(request)
    return redirect('home')

