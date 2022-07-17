from pyexpat import model
from django import forms
from django.contrib import admin
from .models import Material
from contenido.models import Contenido
from documento.models import Documento
from persona.models import Persona
# Register your models here.
from nested_admin import NestedTabularInline, NestedModelAdmin



class DocumentoInline(NestedTabularInline):
  #fields = ('name', 'content')
  model = Documento
  per_page = 0
class ContenidoInline(NestedTabularInline):
 
  #fields = ('name', 'descripcion')
  model = Contenido
  inlines=[DocumentoInline,]
  per_page = 0
@admin.register(Material)
class MaterialAdmin(NestedModelAdmin):
  readonly_fields = ('created', 'updated')
  search_fields=('title',)
  inlines=[ContenidoInline,]

  #list_editable = ['title','person']
  