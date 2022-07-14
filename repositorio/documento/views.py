from urllib import response
from django.shortcuts import render
from asyncio.windows_events import NULL
from django.http import Http404
from django.shortcuts import  get_list_or_404, get_object_or_404, render
import contenido
from django.views.decorators.clickjacking import xframe_options_sameorigin
from .models import Documento
# Create your views here.

def document(request,document_id): 
   documento=get_object_or_404(Documento,id=document_id)
   response=render(request,"documento/document.html",{'documento':documento})
   response ['Content-Security-Policy'] = "frame-ancestors 'self' http://127.0.0.1:8000/ "
   return response