from django import forms

from .models import Personal


class RegModelForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields =["dni","nombre","apellido","email"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, proveeder = email.split("@")
        dominio, extension = proveeder.split(".")
        if not dominio == "intel":
            raise forms.ValidationError("Por favor utiliza un mail con dominio @intel")
        return email


class RegForm (forms.Form):
    dni = forms.IntegerField()
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField()
