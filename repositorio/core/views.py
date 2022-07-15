from django.shortcuts import render, HttpResponse
from .models import AcercaDe
# Create your views here.
def about(request):
   acercaDe = AcercaDe.objects.all
   return render(request,"core/about.html",{'acercaDe':acercaDe})
def contac(request):
   return render(request,"core/contac.html")
