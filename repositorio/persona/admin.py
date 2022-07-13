from django.contrib import admin
from .models import Titulo , Persona
# Register your models here.
@admin.register(Titulo)
class TituloAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')