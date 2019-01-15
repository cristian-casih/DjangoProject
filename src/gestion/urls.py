from django.urls import path

from . import views

app_name = "personal"

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nuevo_personal',views.PersonalCreate.as_view(),name = 'personal_create'),
    path('editar_personal/<int:pk>/',views.PersonalUpdate.as_view(),name = 'personal_update'),
    path('eliminar_personal/<int:pk>/', views.PersonalDelete.as_view(), name='personal_delete'),
    path('personal/', views.PersonalList.as_view(), name ='personal_list'),
]
