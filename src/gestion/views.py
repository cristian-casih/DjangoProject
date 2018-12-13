from django.shortcuts import render

from .forms import RegForm
from .models import Personal

# Create your views here.

def inicio(request):
    form = RegForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        abc = form_data.get('dni')
        abc1 = form_data.get('nombre')
        abc2 = form_data.get('apellido')
        abc3 = form_data.get('email')
        obj = Personal.objects.create(dni=abc, nombre=abc1, apellido=abc2, email=abc3 )
    context = {
        "el_form": form,
    }
    return render(request, "inicio.html", context)
