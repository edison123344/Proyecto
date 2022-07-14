from ipaddress import ip_address
from turtle import back
from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField
from persona.models import Persona
# Create your models here.
class Material(models.Model):
    title = models.CharField(max_length=200,verbose_name="Titulo de la materia")
    duration=models.CharField(max_length=200,verbose_name="Duracion de la materia",null=True, blank=True)
    level=models.CharField(max_length=200,verbose_name="Nivel de la materia",null=True, blank=True)
    description = RichTextField( verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="materia", null=True, blank=True)
    person = models.ForeignKey(Persona, verbose_name="Autor", on_delete=models.CASCADE ,null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    class Meta:
        verbose_name = "material"
        verbose_name_plural = "materiales"
        ordering = ['title']
    

    def __str__(self):
        return self.title
