from django.urls import path
from . import views

urlpatterns = [
    #path('Contenido/', views.Content, name="Contenido"),
    path('document/<int:document_id>/', views.document, name="document"),
]
