from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('personal/', views.PersonalList.as_view(), name='personal')
]
