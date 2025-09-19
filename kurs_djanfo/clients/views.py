# clients/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Client

class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'clients/client_list.html'
    context_object_name = 'clients'

    def get_queryset(self):
        return Client.objects.filter(owner=self.request.user)

class ClientDetailView(LoginRequiredMixin, DetailView):  # Добавьте это представление
    model = Client
    template_name = 'clients/client_detail.html'
    context_object_name = 'client'

    def get_queryset(self):
        return Client.objects.filter(owner=self.request.user)

class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = ['name', 'email', 'phone', 'address', 'comment']
    template_name = 'clients/client_form.html'
    success_url = reverse_lazy('clients:list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ['name', 'email', 'phone', 'address', 'comment']
    template_name = 'clients/client_form.html'
    success_url = reverse_lazy('clients:list')

    def get_queryset(self):
        return Client.objects.filter(owner=self.request.user)

class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'clients/client_confirm_delete.html'
    success_url = reverse_lazy('clients:list')

    def get_queryset(self):
        return Client.objects.filter(owner=self.request.user)