from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import Personalform, Inventarioform
from .models import Personal, Inventario
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.core.paginator import Paginator ,EmptyPage, PageNotAnInteger




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
    # def get_queryset(self):
    #     result = super(PersonalList, self).get_queryset()
    #
    #     query = self.request.GET.get('q')
    #     if query:
    #         result = Personal.objects.filter(nombre__icontains=query)
    #
    #     return result


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
    context_object_name = 'inventario'
    paginate_by = 10
    queryset = Inventario.objects.all()

    def get_queryset(self):
        return Inventario.objects.filter(estadoactivo=True).order_by('id')



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


def search(request):
    queryset_list = Personal.objects.all()
    query = request.GET.get('q')
    if query:

        queryset_list = queryset_list.filter(
            Q(dni__icontains=query) |
            Q(nombre__icontains=query) |
            Q(apellido__icontains=query)
            ).distinct()

    paginator = Paginator(queryset_list, 2)
    page_request_var = "page"
    page=request.GET.get(page_request_var)
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)


    context = {
        "object_list": queryset_list,
        "results": results,
        "page_request_var":page_request_var,
    }
    return render(request, 'gestion/personal_list.html',context)
    # def get_queryset(self):
    #     result = super(PersonalList, self).get_queryset()
    #
    #     query = self.request.GET.get('q')
    #     if query:
    #         result = Personal.objects.filter(nombre__icontains=query)
    #
    #     return result