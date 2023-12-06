from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'username': 'Логин',
                  'email': 'E-mail',
                  'password1': 'Пароль',
                  'password2': 'Подтверждение пароля',
                  }
