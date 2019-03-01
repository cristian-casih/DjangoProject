
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

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
    	return self.name


class Supervisor(models.Model):
    user = models.ForeignKey(User,null=True,blank=True,related_name="supervisor")
    task = models.ManyToManyField(Task,related_name='tasks')

    def __str__(self):

    	return self.user.username
