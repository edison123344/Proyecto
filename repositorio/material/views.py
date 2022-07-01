from django.http import Http404
from django.shortcuts import get_list_or_404, render, HttpResponse
from .models import Material,Tema
from django.shortcuts import render, get_object_or_404
# Create your views here.
def home(request):
   material = Material.objects.all()
   temas = Tema.objects.all
   #print (material)
   #material=get_list_or_404(Material, published=True)
   return render(request,"material/home.html",{'material':material,'temas':temas})
def material(request,material_id):
   
   material = get_object_or_404(Material, id=material_id)
   print(material);
   return render(request,"material/material.html",{'material':material})
def document(request):
   
   return render(request,"material/document.html")
def dowload(request):
   return render(request,"material/download.html")
def list(request):
   return render(request,"material/list.html")
def syllabus(request):
   return render(request,"material/syllabus.html")

 