from django.shortcuts import render, HttpResponse
from .models import Material,Tema
from django.shortcuts import render, get_object_or_404
# Create your views here.
def home(request):
   temas = Tema.objects.all()
   #material=get_object_or_404(Material,Tema.objects.all())
   return render(request,"material/home.html",{'temas':temas})
def material(request,material_id):
   material=get_object_or_404(Material, id=material_id) 
   tema= Tema.object.filter(material=material)
   return render(request,"material/material.html",{'material':material},{'tema':tema})
def document(request):
   
   return render(request,"material/document.html")
def dowload(request):
   return render(request,"material/download.html")
def list(request):
   return render(request,"material/list.html")
def syllabus(request):
   return render(request,"material/syllabus.html")

 