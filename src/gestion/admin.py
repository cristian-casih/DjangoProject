from django.contrib import admin

# Register your models here.
from . models import Personal, Inventario

class AdminPersonal(admin.ModelAdmin):
    list_display= ["dni","nombre","apellido"]
    search_fields = ["dni"]

    class Meta:
        model = Personal

admin.site.register(Personal, AdminPersonal)
admin.site.register(Inventario)