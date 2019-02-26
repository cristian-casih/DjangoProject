from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from usuario.forms import RegistroForm

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class RegistroUsuario(LoginRequiredMixin,CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = User
    template_name = "usuario/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy("gestion:personal_list")

class InventarioCreate(LoginRequiredMixin,CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'