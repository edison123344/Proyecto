from turtle import back
from django.db import models
from django.utils.timezone import now

# Create your models here.
class carrera(models.Model):
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
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'contenido_{0}/{1}'.format(instance.user.id, filename)
    
class contenido(models.Model):
    
    name = models.CharField(max_length=200,verbose_name="Tipo del Contenido")
    uploadedFile = models.FileField(upload_to = "Contenido/",blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "contenido"
        verbose_name_plural = "contenidos"
        ordering = ['name']

    def __str__(self):
        return self.name
class titulo(models.Model):
    
    name = models.CharField(max_length=200,verbose_name="Titulo")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "titulo"
        verbose_name_plural = "titulos"
        ordering = ['name']

    def __str__(self):
        return self.name

class persona(models.Model):
    
    name = models.CharField(max_length=200,verbose_name="Nombre")
    lastname = models.CharField(max_length=200,verbose_name="Apellido")
    titulo = models.ForeignKey(titulo, verbose_name="Titulo", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "persona"
        verbose_name_plural = "personas"
        ordering = ['name']

    def __str__(self):
        return self.name
class silabo(models.Model):
    
    name = models.CharField(max_length=200,verbose_name="Nombre Tema")
    descripcion = models.TextField(verbose_name="Descripcion")
    carrera = models.ForeignKey(carrera, verbose_name="Carrera", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "silabo"
        verbose_name_plural = "silabos"
        ordering = ['name']

    def __str__(self):
        return self.name
class material(models.Model):
    title = models.CharField(max_length=200,verbose_name="Titulo")
    descripcion = models.TextField( verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="materia", null=True, blank=True)
    persona = models.ForeignKey(persona, verbose_name="Autor", on_delete=models.CASCADE)
    silabo = models.ForeignKey(silabo, verbose_name="Silabo", on_delete=models.CASCADE)
    contenido = models.ForeignKey(contenido, verbose_name="Contenido", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "material"
        verbose_name_plural = "materias"
        ordering = ['title']

    def __str__(self):
        return self.title