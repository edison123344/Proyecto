from django.urls import path
from . import views

urlpatterns = [
    path('contac', views.contac, name="contac"),
]

