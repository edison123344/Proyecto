from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('material/<int:material_id>/', views.material, name="material"),
    path('temasContenido/<int:temasContenido_id>/', views.temasContenido, name="temasContenido"),
    #pediente 
    path('contenido/<int:contenido_id>/', views.contenido, name="contenido"),
    
    path('list', views.list, name="list"),
]