from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hola, estan en el index de la app de distancia social")

def camaras(request):
    response = "You're looking at the camaras"
    return HttpResponse(response)

def localidades(request):
    response = "You're looking at the localidades"
    return HttpResponse(response)