
from django.db import models
from django.contrib.auth.models import User
from actstream import registry
from django.apps import AppConfig
# Create your models here.

# class MyModel(models.Model):
#     ...
#
# # Django < 1.7
# registry.register(MyModel)
#
# class MyAppConfig(AppConfig):
#     name = 'usuario'
#
#     def ready(self):
#
#         registry.register(self.get_model('MyModel'))

class Tarea(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
    	return self.name


class Supervisor(models.Model):
    usuario = models.ForeignKey(User, null=True,blank=True, related_name="supervisor")
    tarea = models.ManyToManyField(Tarea, related_name='tarea')

    def __str__(self):

    	return self.user.username
