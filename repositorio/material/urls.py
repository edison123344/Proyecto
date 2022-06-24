from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('descripcionRep', views.descripcionRep, name="descripcionRep"),
    path('document', views.document, name="document"),
    path('list', views.list, name="list"),
    path('dowload', views.dowload, name="dowload"),
    path('syllabus', views.dowload, name="syllabus"),
]