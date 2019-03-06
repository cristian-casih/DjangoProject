from django.apps import AppConfig
from actstream import registry


class UserConfig(AppConfig):
    name = 'usuario'


    def ready(self):
        registry.register(self.get_model('Tarea'),self.get_model('Supervisor'))

