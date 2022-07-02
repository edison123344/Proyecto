from django.http import Http404
from django.shortcuts import get_list_or_404, render, HttpResponse
from .models import Material,Tema,TemasContenido,Contenido
from django.shortcuts import render, get_object_or_404
# Create your views here.
def home(request):
   material = Material.objects.all()
   temas = Tema.objects.all
   return render(request,"material/home.html",{'material':material,'temas':temas})
def material(request,material_id): 
   material = get_object_or_404(Material, id=material_id)
   return render(request,"material/material.html",{'material':material})
def temasContenido(request,temasContenido_id):
   temasContenido=get_object_or_404(TemasContenido, id=temasContenido_id)
   return render(request,"material/content.html",{'temasContenido':temasContenido})
def contenido(request,contenido_id):
   contenido=get_object_or_404(Contenido, id=contenido_id)
   return render(request,"material/download.html",{'contenido':contenido})


def list(request):
   return render(request,"material/list.html")


 