from __future__ import unicode_literals
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.
class Personal(models.Model):
    dni = models.IntegerField(default=0, null=True, blank= True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    apellido = models.CharField(max_length=100, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    email = models.EmailField()
    estadoactivo = models.BooleanField(default=True,null=True, blank=True, editable=True)

    def __str__(self):
        return "{}".format(self.apellido)


class Inventario(models.Model):
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE,)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    numeroserie = models.IntegerField(null=True, blank=True)
    estadoactivo = models.BooleanField(default=True,null=True, blank=True, editable=True)
    imagen = models.ImageField(blank=True, null=True, upload_to="inventario")
    descripcion = models.TextField()

def get_personal(models.Model):

    content_type = ContentType.objects.get_for_model(commission)
    persona = Personal.objects.filter(
        content_type=content_type,
        object_id=commission.id,
        date_to__gte=date.today()
    )

class Activities(models.Model):

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

