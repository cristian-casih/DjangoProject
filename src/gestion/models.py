from __future__ import unicode_literals
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
#from activity.models import Activity
from django.contrib.auth.models import User


# Create your models here.
class Personal(models.Model):
    dni = models.IntegerField(default=0, null=True, blank= True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    apellido = models.CharField(max_length=100, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    email = models.EmailField()
    estadoactivo = models.BooleanField(default=True,null=True, blank=True, editable=True)
    pub_date = models.DateTimeField(default=timezone.now)
    #activity = GenericRelation(Activity, related_query_name="personal")
    activity = GenericRelation('Activity')

    def __str__(self):
        return "{}".format(self.apellido)


class Inventario(models.Model):
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE,)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    numeroserie = models.IntegerField(null=True, blank=True)
    estadoactivo = models.BooleanField(default=True,null=True, blank=True, editable=True)
    imagen = models.ImageField(blank=True, null=True, upload_to="inventario")
    descripcion = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    activity = GenericRelation('Activity')


class Activity(models.Model):
    actor = models.ForeignKey(User, on_delete=models.CASCADE,)
    #verb = models.PositiveIntegerField(choices=VERB_TYPE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    pub_date = models.DateTimeField(default=timezone.now)

    def get_activity():
        content_type = ContentType.objects.get_for_model(Inventario)
        activities = Activity.objects.filter(
            content_type=content_type,
            object_id=Inventario.id,
            date_to__gte=models.DateField.today()
        )

        return activities

# class Activity(models.Model):
#     ASIGNADO= 'A'
#     ACT='B'
#     ACTIVITY_TYPES = (
#         (ASIGNADO, 'Asignado'),
#         (ACT,'Actividad')
#     )
#
#     inventario = ContentType.objects.get_for_model(Inventario)
#     activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPES)
#     date = models.DateTimeField(auto_now_add=True)
#
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')
#
#     def get_activity():
#         inventario = Inventario.objects.filter(
#             content_type=content_type,
#             object_id=Inventario.id,
#             date_to__gte=models.DateField.today()
#     )
#
#         return inventario
#

# class Activity(models.Model):
#     FAVORITE = 'F'
#     LIKE = 'L'
#     UP_VOTE = 'U'
#     DOWN_VOTE = 'D'
#     ACTIVITY_TYPES = (
#         (FAVORITE, 'Favorite'),
#         (LIKE, 'Like'),
#         (UP_VOTE, 'Up Vote'),
#         (DOWN_VOTE, 'Down Vote'),
#     )
#
#     user = models.ForeignKey(User)
#     activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPES)
#     date = models.DateTimeField(auto_now_add=True)
#
#     # Below the mandatory fields for generic relation
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey()