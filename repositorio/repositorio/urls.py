
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from core import views 
urlpatterns = [
    # Paths de contenido
    path('', include('contenido.urls')),
    # Paths de materia
    path('', include('material.urls')),
    # Paths del core
    path('core/', include('core.urls')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
