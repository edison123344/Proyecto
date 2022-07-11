from pyexpat import model
from django import forms
from django.contrib import admin
from .models import Material, Carrera ,Contenido,TemasContenido,Titulo, Persona,Tema

# Register your models here.
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
  #readonly_fields = ('created', 'updated')
  search_fields=('title',)
  #list_editable = ['title','persona']
  ##def formfield_for_manytomany(self, db_field, request, **kwargs):
   #if db_field.name == "contenido":
      #kwargs["queryset"] = Material.temasContenido_set.all()
    #return super().formfield_for_manytomany(db_field, request, **kwargs)

@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')

@admin.register(Contenido)
class ContenidoAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')

@admin.register(Titulo)
class TituloAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')

@admin.register(Tema)
class TemaAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')

@admin.register(TemasContenido)
class TemaContenidoAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')
 
