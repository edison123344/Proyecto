from django.contrib import admin
from .models import Tema
# Register your models here.
@admin.register(Tema)
class TemaAdmin(admin.ModelAdmin):
  readonly_fields = ('created', 'updated')