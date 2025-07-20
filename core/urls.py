# core/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .forms import LoginForm 
from .views import logout_view


app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('contactsuccess/', TemplateView.as_view(template_name='core/contactsuccess.html'), name='contactsuccess'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm ), name='login'),
    path('logout/', logout_view, name='logout'),
]