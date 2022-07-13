from django.urls import path
from . import views

urlpatterns = [
    #path('Contenido/', views.Content, name="Contenido"),
    path('contentDescription/<int:material_id>/', views.contentDescription, name="contentDescription"),
    path('content/<int:contenido_id>/', views.content, name="content"),

]

