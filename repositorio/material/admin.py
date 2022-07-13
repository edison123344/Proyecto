from pyexpat import model
from django import forms
from django.contrib import admin
from .models import Material
from contenido.models import Contenido
# Register your models here.

class ContenidoInline(admin.TabularInline):
    model = Contenido
    extra = 1

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')
  search_fields=('title',)
  inlines=[ContenidoInline,]

  #list_editable = ['title','persona']
  