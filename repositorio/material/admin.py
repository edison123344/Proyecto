from pyexpat import model
from django.contrib import admin
from .models import Material, Carrera ,Contenido,TemasContenido,Titulo, Persona,Tema

# Register your models here.

class MaterialAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')
class CarreraAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')
class ContenidoAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')
class TituloAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')
class PersonaAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')
class TemaAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')
class TemaContenidoAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')
 
admin.site.register(Material, MaterialAdmin)
admin.site.register(Carrera,CarreraAdmin)
admin.site.register(Contenido,ContenidoAdmin)
admin.site.register(Titulo,TituloAdmin)
admin.site.register(Persona,PersonaAdmin)
admin.site.register(Tema,TemaAdmin)
admin.site.register(TemasContenido,TemaContenidoAdmin)