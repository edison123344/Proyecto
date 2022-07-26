


from django.shortcuts import  get_object_or_404, render
from material.models import Material
from .models import Contenido
# Create your views here.

def contentDescription(request,material_id): 
   MaterialDes=get_object_or_404(Material,id=material_id)
   return render(request,"contenido/contentDescription.html",{'material':MaterialDes})
def content(request,contenido_id):
   ContenidoDes=get_object_or_404(Contenido,id=contenido_id) 
   return render(request,"contenido/content.html",{'contenidoDes':ContenidoDes})