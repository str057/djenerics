from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from .models import User
from .forms import UserRegisterForm, UserProfileForm


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, 'Регистрация прошла успешно!')
        return redirect('index')


class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True  # Перенаправлять если уже авторизован

    def get_success_url(self):
        return reverse_lazy('index')

    def form_valid(self, form):
        messages.success(self.request, 'Вы успешно вошли в систему!')
        return super().form_valid(form)


def logout_view(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из системы!')
    return redirect('index')


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'registration/profile.html'

    def get_success_url(self):
        return reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Профиль успешно обновлен!')
        return super().form_valid(form)