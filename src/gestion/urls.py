from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = "gestion"

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nuevopersonal', login_required(views.PersonalCreate.as_view()), name='personal_create'),
    path('editarpersonal/<int:pk>/', login_required(views.PersonalUpdate.as_view()), name = 'personal_form'),
    path('eliminarpersonal/<int:pk>/', login_required(views.PersonalDelete.as_view()), name='personal_delete'),
    path('personal/', login_required(views.PersonalList.as_view()), name ='personal_list'),
    path('prueba/<int:pk>/', login_required(views.personal_inv), name='personal_inv'),
    path('personalinv/<int:pk>/', login_required(views.PersonalIList.as_view()), name='personal_inv'),
    path('inventario/', login_required(views.InventarioList.as_view()), name='inventario_list'),
    path('nuevoinventario', login_required(views.InventarioCreate.as_view()), name='inventario_form'),
    path('editarinventario/<int:pk>/', login_required(views.InventarioUpdate.as_view()), name='inventario_form'),
    path('eliminarinventario/<int:pk>/', login_required(views.InventarioDelete.as_view()), name='inventario_delete'),


]
