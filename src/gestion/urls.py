from django.urls import path

from . import views

app_name = "gestion"

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nuevopersonal', views.PersonalCreate.as_view(), name='personal_create'),
    path('editarpersonal/<int:pk>/', views.PersonalUpdate.as_view(), name = 'personal_form'),
    path('eliminarpersonal/<int:pk>/', views.PersonalDelete.as_view(), name='personal_delete'),
    path('personal/', views.PersonalList.as_view(), name ='personal_list'),
    path('personalinv/<int:pk>/', views.personal_inv, name='personal_inv'),
    path('inicioinventario', views.index_inventario, name='inicioinventario'),
    path('inventario/', views.InventarioList.as_view(), name='inventario_list'),
    path('nuevoinventario', views.InventarioCreate.as_view(), name='inventario_form'),

]
