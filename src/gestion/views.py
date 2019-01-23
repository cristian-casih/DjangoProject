from django.shortcuts import render, redirect
from .forms import Personalform, Inventarioform
from .models import Personal, Inventario
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def inicio(request):
    titulo = "Hola"
    if request.user.is_authenticated:
        titulo = "Bienvenido %s" %(request.user)
    #
    # form = RegModelForm(request.POST or None)
    #
    # context = {
    #     "titulo": titulo,
    #     "el_form": form,
    # }
    # # if form.is_valid():
    # #     apellido = form.cleaned_data.get("apellido")
    # #     form.save()
    # #     context = {
    # #         "titulo": "Registrado con exito %s!" %(apellido)
    # #     }
    # #
    # # return render(request, "gestion/inicio.html", context)
    # if form.is_valid():
    #     form.save()
    #
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

    def get_queryset(self):
        return Personal.objects.filter(estadoactivo=True).order_by('id')


def personal_inv(request):
    inventario= Inventario.objects.all(pk=id)
    contexto = {'inventario': inventario}

    return render(request, "gestion/personal_inv.html", contexto)


def index_inventario(request):
    return HttpResponse("Pagina inventario")


class InventarioList(ListView):
    model= Inventario
    template_name = 'gestion/inventario_list.html'

    def get_queryset(self):
        return Inventario.objects.all


class InventarioCreate(CreateView):
    model = Inventario
    template_name = 'gestion/inventario_form.html'
    form_class = Inventarioform
    second_form_class = Personalform
    success_url = reverse_lazy('gestion:inventario_list')

    def get_context_data(self, **kwargs):
        context = super(InventarioCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            inventario = form.save(commit=False)
            inventario.personal = form2.save()
            inventario.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))