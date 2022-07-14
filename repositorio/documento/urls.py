from django.urls import path
from . import views
from django.conf import settings
urlpatterns = [
    #path('Contenido/', views.Content, name="Contenido"),
    path('document/<int:document_id>/', views.document, name="document"),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
