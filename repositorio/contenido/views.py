
from asyncio.windows_events import NULL
from django.http import Http404
from django.shortcuts import  get_list_or_404, get_object_or_404, render
import contenido
from material.models import Material
from documento.models import Documento
from .models import Contenido
# Create your views here.

def contentDescription(request,material_id): 
   MaterialDes=get_object_or_404(Material,id=material_id)
   return render(request,"contenido/contentDescription.html",{'material':MaterialDes})
def content(request,contenido_id):
   ContenidoDes=get_object_or_404(Contenido,id=contenido_id)
   #documentos=get_object_or_404(Documento,id=contenido_id)
   return render(request,"contenido/content.html",{'contenidoDes':ContenidoDes})