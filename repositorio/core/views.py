from django.shortcuts import render, HttpResponse
from .models import AcercaDe
# Create your views here.
def about(request):
   acercaDe = AcercaDe.objects.all
   return render(request,"core/about.html",{'acercaDe':acercaDe})
def terms (request):
   return render(request,"core/privacy-and-terms-of-use.html")