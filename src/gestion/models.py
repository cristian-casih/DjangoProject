from __future__ import unicode_literals

from django.db import models
import datetime

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
        return "{}".format(self.id)


class Inventario(models.Model):
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE,)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    numeroserie = models.IntegerField(null=True, blank=True)
    estadoactivo = models.BooleanField(default=True,null=True, blank=True, editable=True)
    #imagen = models.ImageField(blank=True, null=True, verbose_name='Photo')
    descripcion = models.TextField()
