from django.urls import path

from . import views

app_name = "usuario"

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar', views.RegistroUsuario.as_view(), name='registrar_usuario'),
]
