from turtle import title
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class AcercaDe(models.Model):
    title= models.CharField(max_length=200,verbose_name="Titulo")
    description = RichTextField( verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "AcercaDe"
        verbose_name_plural = "AcercaDe"
        ordering = ['title']

    def __str__(self):
        return self.title
