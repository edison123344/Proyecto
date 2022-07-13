from django.db import models

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'contenido_{0}/{1}'.format(instance.user.id, filename)
    
class Documento(models.Model):
    
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