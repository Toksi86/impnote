from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'username': 'Имя пользователя',
                  'email': 'E-mail',
                  'password1': 'Пароль',
                  'password2': 'Подтверждение пароля',
                  }
