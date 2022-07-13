from django.shortcuts import render, HttpResponse

# Create your views here.
def about(request):
   return render(request,"core/about.html")
def contac(request):
   return render(request,"core/contac.html")

'''lista =NULL
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
   #pendiente
def contenido(request,contenido_id):
   contenido=get_object_or_404(Contenido, id=contenido_id)
   return render(request,"material/download.html",{'contenido':contenido})


def list(request):
   busqueda =request.GET.get('buscar')
   if busqueda:
      temas=Tema.objects.filter(Q(title__icontains=busqueda)
      ).distinct()
      materiales=Material.objects.filter(Q(title__icontains=busqueda)|
      Q(persona__name__icontains=busqueda)
      ).distinct()
   return render(request,"material/list.html",{'temas':temas,'materiales':materiales})'''