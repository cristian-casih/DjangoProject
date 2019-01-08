from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Personal (models.Model):

    dni = models.IntegerField(default=0, null=True, blank= True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    apellido = models.CharField(max_length=100, null=True, blank=True)

    email = models.EmailField()
    estadoactivo = models.BooleanField(default=True, editable=False)

    def __str__(self):
        return self.email


class Inventario(models.Model):
    personal = models.ForeignKey('Personal',on_delete=models.CASCADE,)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    numeroserie = models.IntegerField()
    estadoactivo = models.BooleanField(default=True, editable=False)
    #imagen = models.ImageField(blank=True, null=True, verbose_name='Photo')
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre