from asyncio.windows_events import NULL
from django.http import Http404
from django.shortcuts import  render
from .models import Material
from django.db.models import Q

# Create your views here.
def home(request):
   materiales = Material.objects.all()
  
   return render(request,"material/home.html",{'materiales':materiales})

