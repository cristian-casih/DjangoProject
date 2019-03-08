from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'user_id'
            'username',
            'first_name',
            'last_name',
            'email',

        ]
        labels = {
            'user_id' : 'id del usuario',
            'username': 'Nombre de usuario',
            'first_name':'Nombre',
            'last_name':'Apellido',
            'email':'Email',

        }