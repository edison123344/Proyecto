from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('material/<int:material_id>/', views.material, name="material"),

    path('document', views.document, name="document"),
    path('list', views.list, name="list"),
    path('dowload', views.dowload, name="dowload"),
    path('syllabus', views.dowload, name="syllabus"),
]