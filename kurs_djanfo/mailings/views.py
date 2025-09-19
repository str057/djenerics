from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from django.core.mail import send_mail
from django.utils import timezone
from .models import Mailing, MailingAttempt
from .forms import MailingForm
from clients.models import Client
from messages_app.models import Message


def index(request):
    """
    Главная страница приложения
    """
    from django.utils import timezone
    now = timezone.now()


    active_mailings = Mailing.objects.filter(
        status='started',
        start_time__lte=now,
        end_time__gte=now
    )

    context = {
        'total_mailings': Mailing.objects.count(),
        'active_mailings': active_mailings.count(),
        'unique_clients': Client.objects.values('email').distinct().count()
    }
    return render(request, 'index.html', context)


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    template_name = 'mailings/mailing_list_new.html'
    context_object_name = 'mailings'

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)

class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing
    template_name = 'mailings/mailing_detail.html'

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['attempts'] = MailingAttempt.objects.filter(mailing=self.object)
        return context


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    template_name = 'mailings/mailing_confirm_delete.html'
    success_url = reverse_lazy('mailings:mailing_list')

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailings/mailing_form_simple.html'
    success_url = reverse_lazy('mailings:mailing_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['clients'].queryset = Client.objects.filter(owner=self.request.user)

        return form

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)

        try:

            mailing = Mailing.objects.get(pk=self.object.pk)
            mailing.send_mailing()
            messages.success(self.request, 'Рассылка создана и отправлена!')
        except Exception as e:
            messages.warning(self.request, f'Рассылка создана, но возникла ошибка при отправке: {e}')

        return response

class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailings/mailing_form_simple.html'
    success_url = reverse_lazy('mailings:mailing_list')

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Передаем пользователя в форму
        return kwargs


def send_mailing_now(request, pk):
    """Функция для ручной отправки рассылки"""
    try:
        mailing = Mailing.objects.get(id=pk, owner=request.user)

        # Проверяем права доступа
        if mailing.owner != request.user:
            messages.error(request, 'У вас нет прав для отправки этой рассылки')
            return redirect('mailings:mailing_list')

        # Отправляем рассылку
        mailing.send_mailing()
        messages.success(request, 'Рассылка отправлена успешно!')

    except Mailing.DoesNotExist:
        messages.error(request, 'Рассылка не найдена')
    except Exception as e:
        messages.error(request, f'Ошибка при отправке: {e}')

    return redirect('mailings:mailing_detail', pk=pk)