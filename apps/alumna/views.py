from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

#def pestañaNoticias(request):
   # return render(request, "pestañaNoticias.html")

def index(request):
    return HttpResponse("EN ESTE MODULO PUEDEN DESCARGAR SUS GUIAS Y ACTIVIDADES")
