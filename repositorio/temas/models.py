from django.db import models
from material.models import Material
# Create your models here.
class Tema(models.Model):
    title = models.CharField(max_length=200,verbose_name="Titulo del Tema")
    material = models.ManyToManyField(Material, verbose_name="Material", related_name="tema", blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "tema"
        verbose_name_plural = "temas"
        ordering = ['title']

    def __str__(self):
        return self.title