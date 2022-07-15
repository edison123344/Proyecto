from asyncio.windows_events import NULL
from django.http import Http404
from django.shortcuts import  render
from .models import Material
from django.db.models import Q
from temas.models import Tema
# Create your views here.
def home(request):
   materiales = Material.objects.all()
   temas = Tema.objects.all
   return render(request,"material/home.html",{'materiales':materiales,'temas':temas})

def list(request):
   busqueda =request.GET.get('buscar') 
   temasGeneral = Tema.objects.all
   if busqueda:
      temas=Tema.objects.filter(Q(title__icontains=busqueda)
      ).distinct()
      material=Material.objects.filter(Q(title__icontains=busqueda)|
      Q(person__name__icontains=busqueda)
      ).distinct()
   return render(request,"material/list.html",{'temas':temas,'materiales':material,'teamasGeneral':temasGeneral})
   