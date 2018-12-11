from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Personal (models.Model):
    #dni = models.BigAutoField(max_length= 100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.apellido

