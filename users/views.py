from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm


def sign_up(request):
    """Регистрирует нового пользователя."""
    if request.method != 'POST':
        form = RegisterForm()
    else:
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user, backend='users.authentication.EmailAuthBackend')
            return redirect('notes:index')
    context = {'form': form}
    return render(request, 'registration/register.html', context)
