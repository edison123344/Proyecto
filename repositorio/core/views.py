from django.shortcuts import render, HttpResponse

# Create your views here.
def about(request):
   return render(request,"core/about.html")
def contac(request):
   return render(request,"core/contac.html")