
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from core import views 
urlpatterns = [
    # Paths de documento
    path('', include('documento.urls')),
    # Paths de contenido
    path('', include('contenido.urls')),
    # Paths de materia
    path('', include('material.urls')),
    # Paths del core
    path('core/', include('core.urls')),
    path('admin/', admin.site.urls),
     path('_nested_admin/', include('nested_admin.urls')),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header="REPGNU"
admin.site.index_title="Panel de Administrador"
admin.site.site_title="REPGNU"