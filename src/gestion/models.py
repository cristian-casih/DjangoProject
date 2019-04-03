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


#
# class Activity(models.Model):
#
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')
#
#
# def get_activities():
#
#     content_type = ContentType.objects.get_for_model(Inventario)
#     inventario = Inventario.objects.filter(
#         content_type=content_type,
#         object_id=Inventario.id,
#         date_to__gte=models.DateField.today()
#     )
#
#     return inventario


class Activity(models.Model):
    ASIGNADO= 'A'
    ACT='B'
    ACTIVITY_TYPES = (
        (ASIGNADO, 'Asignado'),
        (ACT,'Actividad')
    )

    inventario = ContentType.objects.get_for_model(Inventario)
    activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPES)
    date = models.DateTimeField(auto_now_add=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def get_activity():
        inventario = Inventario.objects.filter(
            content_type=content_type,
            object_id=Inventario.id,
            date_to__gte=models.DateField.today()
    )

        return inventario



#[11:13, 15/3/2019] Pablo Vates: agregues 2 metodos. uno que reciba el objeto y le agregue al objeto el contenttype y el contentid
#[11:14, 15/3/2019] Pablo Vates: y en el objeto que estas agregando las actividad, por ejemplo en el inventario agrega un metodo que
#sea algo asi como get_activity que filtre las actividade sy devuelva la lista de actividades relacionadas al objeto
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