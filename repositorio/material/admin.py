from pyexpat import model
from django.contrib import admin
from .models import material, carrera ,contenido, silabo ,titulo, persona, silabo

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
class SilaboAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')
 
admin.site.register(material, MaterialAdmin)
admin.site.register(carrera,CarreraAdmin)
admin.site.register(contenido,ContenidoAdmin)
admin.site.register(titulo,TituloAdmin)
admin.site.register(persona,PersonaAdmin)
admin.site.register(silabo,SilaboAdmin)