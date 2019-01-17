from django.urls import path

from . import views

app_name = "personal"

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nuevopersonal', views.PersonalCreate.as_view(), name='personal_create'),
    path('editarpersonal/<int:pk>/', views.PersonalUpdate.as_view(), name = 'personal_form'),
    path('eliminarpersonal/<int:pk>/', views.PersonalDelete.as_view(), name='personal_delete'),
    path('personal/', views.PersonalList.as_view(), name ='personal_list'),
]
