from ipaddress import ip_address
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
    titulo = models.ForeignKey(Titulo, verbose_name="Titulo", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "persona"
        verbose_name_plural = "personas"
        ordering = ['name']

    def __str__(self):
        return self.name
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'contenido_{0}/{1}'.format(instance.user.id, filename)
    
class Contenido(models.Model):
    
    name = models.CharField(max_length=200,verbose_name="Nombre del Contenido")
    uploadedFile = models.FileField(upload_to = "Contenido/",blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "contenido"
        verbose_name_plural = "contenidos"
        ordering = ['name']

    def __str__(self):
        return self.name
class TemasContenido(models.Model):
    
    name = models.CharField(max_length=200,verbose_name="Tipo del Contenido")
    descripcion = RichTextField( verbose_name="Descripcion")
    contenido = models.ManyToManyField(Contenido, verbose_name="Contenido", related_name="get_posts",blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "tipocontenido"
        verbose_name_plural = "tiposcontenidos"
        ordering = ['name']

    def __str__(self):
        return self.name
class Material(models.Model):
    title = models.CharField(max_length=200,verbose_name="Titulo de la materia")
    descripcion = RichTextField( verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="materia", null=True, blank=True)
    persona = models.ForeignKey(Persona, verbose_name="Autor", on_delete=models.CASCADE)
    contenido = models.ManyToManyField(TemasContenido, verbose_name="Contenido", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    class Meta:
        verbose_name = "material"
        verbose_name_plural = "materiales"
        ordering = ['title']

    def __str__(self):
        return self.title
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
        return self.title
        