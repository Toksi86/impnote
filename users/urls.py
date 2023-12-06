"""Определяет схемы URL для пользователей"""

from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.sign_up, name='register'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', views.activate,
         name='activate'),
    path('email_confirm', views.email_confirm, name='email_confirm'),
    path('email_confirm_filed', views.email_confirm_filed, name='email_confirm_filed'),
]
