from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = "gestion"

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nuevopersonal', views.PersonalCreate.as_view(), name='personal_create'),
    path('editarpersonal/<int:pk>/', views.PersonalUpdate.as_view(), name='personal_form'),
    path('eliminarpersonal/<int:pk>/', views.PersonalDelete.as_view(), name='personal_delete'),
    path('personal/', views.PersonalList.as_view(), name='personal_list'),
    path('invpersonal/<int:personal_id>/', views.personal_inv, name='inv_personal'),
    path('inventario/', views.InventarioList.as_view(), name='inventario_list'),
    path('nuevoinventario', views.InventarioCreate.as_view(), name='inventario_form'),
    path('editarinventario/<int:pk>/', views.InventarioUpdate.as_view(), name='inventario_form'),
    path('eliminarinventario/<int:pk>/',views.InventarioDelete.as_view(), name='inventario_delete'),
    path('resultado/', views.search, name="search"),
    path('resultado_inv/', views.search_inventario, name="searchinventario")

]
