from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import Personalform, Inventarioform
from .models import Personal, Inventario
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.


def inicio(request):
    return render(request, "gestion/inicio.html")


class PersonalCreate(CreateView):
    model = Personal
    form_class = Personalform
    template_name = "gestion/personal_form.html"
    success_url = reverse_lazy("gestion:personal_list")


class PersonalUpdate(UpdateView):
    model = Personal
    form_class = Personalform
    template_name_suffix = "_form"
    success_url = reverse_lazy("gestion:personal_list")


class PersonalDelete(DeleteView):
    model = Personal
    template_name = "gestion/personal_delete.html"
    success_url = reverse_lazy("gestion:personal_list")


class PersonalList(ListView):
    model = Personal
    template_name = 'gestion/personal_list.html'
    context_object_name = 'personal'
    paginate_by = 10
    queryset = Personal.objects.all()

    def get_queryset(self):
        return Personal.objects.filter(estadoactivo=True).order_by('id')


@login_required
def personal_inv(request, personal_id=0):
    context = {}
    if personal_id != '0':
        personal = Personal.objects.get(pk=personal_id)
        inventario = Inventario.objects.filter(personal=personal_id)
        context = {
            "personal": personal,
            "inventario": inventario
        }

    return render(request, "gestion/inv_personal.html",context)


class InventarioList(ListView):
    model = Inventario
    template_name = 'gestion/inventario_list.html'

    def get_queryset(self):
        return Inventario.objects.all


class InventarioCreate(CreateView):
    model = Inventario
    template_name = 'gestion/inventario_form.html'
    form_class = Inventarioform
    success_url = reverse_lazy('gestion:inventario_list')


class InventarioUpdate(UpdateView):
    model = Inventario
    form_class = Inventarioform
    template_name_suffix = "_form"
    success_url = reverse_lazy("gestion:inventario_list")


class InventarioDelete(DeleteView):
    model = Inventario
    template_name = "gestion/inventario_delete.html"
    success_url = reverse_lazy("gestion:inventario_list")
