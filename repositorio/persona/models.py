
from pyexpat import model
from turtle import back
from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField
# Create your models here.
class Titulo(models.Model):
    
    name = models.CharField(max_length=200,verbose_name="Titulo")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "titulo"
        verbose_name_plural = "titulos"
        ordering = ['name']

    def __str__(self):
        return self.name

class Persona(models.Model):
    
    name = models.CharField(max_length=200,verbose_name="Nombre")
    lastname = models.CharField(max_length=200,verbose_name="Apellido")
    mail = models.CharField(max_length=200,verbose_name="Correo" ,null=True, blank=True)
    imge=models.ImageField(verbose_name="Imagen Docente", upload_to="persona", null=True, blank=True)
    titulo = models.ForeignKey(Titulo, verbose_name="Titulo", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "persona"
        verbose_name_plural = "personas"
        ordering = ['name']

    def __str__(self):
        return self.name