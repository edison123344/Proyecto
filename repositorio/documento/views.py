from django.shortcuts import render
from django.shortcuts import   get_object_or_404, render
from .models import Documento
# Create your views here.

def document(request,document_id): 
   documento=get_object_or_404(Documento,id=document_id)
   return render(request,"documento/document.html",{'documento':documento})
  