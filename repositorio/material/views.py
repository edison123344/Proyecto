from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
   return render(request,"material/home.html")
def descripcionRep(request):
   return render(request,"material/descripcionRep.html")
def document(request):
   return render(request,"material/document.html")
def dowload(request):
   return render(request,"material/download.html")
def list(request):
   return render(request,"material/list.html")
def syllabus(request):
   return render(request,"material/syllabus.html")