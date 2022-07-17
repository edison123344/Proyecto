from django.contrib import admin
from .models import Titulo , Persona
# Register your models here.
@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')


#@admin.register(Titulo)
#class PersonaAdmin(admin.ModelAdmin):
  #readonly_fields = ('created', 'updated')