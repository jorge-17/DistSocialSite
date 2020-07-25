from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import CatCamaras, CatLocalidades


# Create your views here.
def index(request):
    return HttpResponse("Hola, estan en el index de la app de distancia social")

def localidades(request):
    lista_localidades = CatLocalidades.objects.order_by('id_CatLocalidad')[:15]
    template = loader.get_template('DistSocialApp/localidades.html')
    context = {
        'lista_localidades': lista_localidades
    }
    
    return HttpResponse(template.render(context, request))

def camaras(request):
    lista_camaras = CatCamaras.objects.order_by('id_CatCamara')[:15]
    template = loader.get_template('DistSocialApp/camaras.html')
    context = {
        'lista_camaras': lista_camaras
    }
    return HttpResponse(template.render(context, request))