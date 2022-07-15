from django.contrib import admin
from .models import AcercaDe
# Register your models here.

@admin.register(AcercaDe)
class TituloAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')
  