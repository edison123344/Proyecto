from django.db import models
from ckeditor.fields import RichTextField
from material.models import Material
# Create your models here.
class Contenido(models.Model):
    TITLE_CHOICES = [
       ('Clases', 'Clases'),
       ('Practicas', 'Practicas'),
       ('Tareas', 'Tareas'),
       ('Tareas', 'Lecciones'),
       ('Examenes', 'Examenes'),
       ('Otros', 'Otros'),
   ]
    name = models.CharField(max_length=200,verbose_name="Tipo del Contenido", choices=TITLE_CHOICES)
    descripcion = RichTextField( verbose_name="Descripcion")
    material = models.ForeignKey(Material, verbose_name="Autor", on_delete=models.CASCADE,null=True, blank=True ,related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "tipocontenido"
        verbose_name_plural = "tiposcontenidos"
        ordering = ['name']

    def __str__(self):
        return self.name