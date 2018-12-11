from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Personal (models.Model):

    dni = models.IntegerField(default=0,null= False,blank= False)
    nombre = models.CharField(max_length=100,null= False,blank= False)
    apellido = models.CharField(max_length=100,null= False,blank= False)
    email = models.EmailField()

    def __str__(self):
        return self.apellido

class Inventario (models.Model):

    id = models.IntegerField(default=0)
    nombre = models.CharField(max_length=100,null= False,blank= False)
    stockinicial = models.IntegerField(default=0)
    stockactual = models.IntegerField(default=0)
    estado = models.BooleanField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre