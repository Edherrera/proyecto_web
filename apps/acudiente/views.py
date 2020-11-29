from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

#def pestañaNoticias(request):
   # return render(request, "pestañaNoticias.html")

def index_acudiente(request):
    return HttpResponse("PAGINA PRINCIPAL DE ACUDIENTES")