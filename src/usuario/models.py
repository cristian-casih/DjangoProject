
from django.db import models
from actstream import registry
from django.apps import AppConfig
# Create your models here.

class MyModel(models.Model):
    ...

# Django < 1.7
registry.register(MyModel)

class MyAppConfig(AppConfig):
    name = 'usuario'

    def ready(self):

        registry.register(self.get_model('MyModel'))