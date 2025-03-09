from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('about/', about, name = 'about'),
    path('assesment/', assesment, name = 'assesment'),
    path('services/', services, name = 'services'),
    path('contact/', contact, name = 'contact'),
    path('register/', register, name = 'register'),
    path('login/', user_login, name = 'login'),
    path('logout/', user_logout, name = 'logout'),
    path('send_email/', send_email, name = 'send_email'),
]