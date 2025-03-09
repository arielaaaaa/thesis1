from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import send_mail
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

def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Construct the email subject and message
        subject = f'New message from {name}'
        email_message = f'{message}'
        
        # Send the email
        send_mail(
            subject,
            email_message,
            settings.DEFAULT_FROM_EMAIL,
            [email],  # Send to the email provided by the user
            fail_silently=False,
        )
        return HttpResponse('Form submitted successfully!')
    return render(request, 'myapp/send-email.html')

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

