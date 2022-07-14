from django.db import models

# Create your models here.
'''from ipaddress import ip_address
from turtle import back
from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField
# Create your models here.
class Carrera(models.Model):
    carrera = models.CharField(max_length=200,verbose_name="Carrera")
    periodo = models.SmallIntegerField(verbose_name="Periodo", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "carrera"
        verbose_name_plural = "carreras"
        ordering = ['carrera']

    def __str__(self):
        return self.carrera

class Tema(models.Model):
    title = models.CharField(max_length=200,verbose_name="Titulo del Tema")
    descripcion = models.CharField(max_length=200, verbose_name="Descripcion")
    material = models.ManyToManyField(Material, verbose_name="Contenido", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "tema"
        verbose_name_plural = "temas"
        ordering = ['title']

    def __str__(self):
        return self.title'''