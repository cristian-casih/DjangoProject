from django.shortcuts import render
from .forms import RegModelForm
from .models import Personal
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.

def inicio(request):
    titulo = "Hola"
    if request.user.is_authenticated:
        titulo = "Bienvenido %s" %(request.user)

    form = RegModelForm(request.POST or None)

    context = {
        "titulo": titulo,
        "el_form": form,
    }
    # if form.is_valid():
    #     apellido = form.cleaned_data.get("apellido")
    #     form.save()
    #     context = {
    #         "titulo": "Registrado con exito %s!" %(apellido)
    #     }
    #
    # return render(request, "gestion/inicio.html", context)
    if form.is_valid():
        form.save()

    return render(request, "gestion/inicio.html", context)

class PersonalCreate(CreateView):
    model = Personal
    form_class = RegModelForm
    template_name = "gestion/personal_create.html"
    success_url = reverse_lazy("personal:personal_list")

class PersonalUpdate(UpdateView):
    model = Personal
    form_class = RegModelForm
    template_name = "gestion/personal_create.html"
    success_url = reverse_lazy("personal:personal_list")

class PersonalDelete(DeleteView):
    model = Personal
    template_name = "gestion/personal_delete.html"
    success_url = reverse_lazy("personal:personal_list")

class PersonalList(ListView):
    model = Personal
    template_name = 'gestion/personal_list.html'

    def get_queryset(self):
        return Personal.objects.filter(estadoactivo=True).order_by('id')
