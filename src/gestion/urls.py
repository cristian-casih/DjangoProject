from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('<int:pk>/personal/', views.PersonalList.as_view(), name='personal')
]
