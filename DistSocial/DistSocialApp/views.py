from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.core import serializers
import json
from django.shortcuts import get_object_or_404, render
from .models import CatCamaras, CatLocalidades, CatUsuarios, CatOrganizaciones, Registros


# Create your views here.
def index(request):    
    #Carga lista de organizaciones
    lista_organizaciones = CatOrganizaciones.objects.order_by('id_CatOrganizacion')
    template = loader.get_template('DistSocialApp/index.html')
    context = {'lista_org' : lista_organizaciones}
    return HttpResponse(template.render(context, request))

def localidades(request):
    lista_localidades = CatLocalidades.objects.order_by('id_CatLocalidad')[:15]
    context = {'lista_localidades': lista_localidades}    
    return render(request, 'DistSocialApp/localidades.html', context)

def camaras(request):
    lista_camaras = CatCamaras.objects.order_by('id_CatCamara')[:15]
    template = loader.get_template('DistSocialApp/camaras.html')
    context = {'lista_camaras': lista_camaras}
    return HttpResponse(template.render(context, request))

def login(request):
    idOrg = request.POST.get('idOrg')
    userName = request.POST.get('userName')
    userPass = request.POST.get('userPass')
    userVal = CatUsuarios.objects.filter(usuario=userName, pw=userPass, id_CatOrganizacion=idOrg).exists()
    #user = CatUsuarios.objects.filter(usuario=userName, pw=userPass, id_CatOrganizacion=idOrg).first()
    #user = serializers.serialize("json", user)
    return JsonResponse(userVal, safe=False)

def grafica1(request):
    registros = Registros.objects.filter(status=True).only('valor', 'creado')
    #print(registros)
    data = serializers.serialize("json", registros)
    #print(data)
    #data = json.dumps(data)
    #print(data)
    return render(request, 'DistSocialApp/grafica1.html', {'dataRegistros': data})

