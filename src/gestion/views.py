from django.shortcuts import render


from .forms import RegModelForm
from .models import Personal

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
    if form.is_valid():
        apellido = form.cleaned_data.get("apellido")
        form.save()
        context = {
            "titulo": "Registrado con exito %s!" %(apellido)
        }



    return render(request, "base.html", context)
