from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader, RequestContext, Template
from django.core import serializers
from django.shortcuts import get_object_or_404, render
from .models import CatCamaras, CatLocalidades, CatUsuarios, CatOrganizaciones, Registros


# Create your views here.
def index(request):    
    lista_organizaciones = CatOrganizaciones.objects.order_by('id_CatOrganizacion')
    context = {'lista_org' : lista_organizaciones}
    return render(request, 'DistSocialApp/index.html', context)

def localidades(request):
    lista_localidades = CatLocalidades.objects.order_by('id_CatLocalidad')[:15]
    context = {'lista_localidades': lista_localidades}    
    return render(request, 'DistSocialApp/localidades.html', context)

def camaras(request):
    lista_camaras = CatCamaras.objects.order_by('id_CatCamara')[:15]
    context = {'lista_camaras': lista_camaras}
    return render(request, 'DistSocialApp/camaras.html', context)

def login(request):
    idOrg = request.POST.get('idOrg')
    userName = request.POST.get('userName')
    userPass = request.POST.get('userPass')
    userVal = CatUsuarios.objects.filter(usuario=userName, pw=userPass, id_CatOrganizacion=idOrg).exists()
    FullNameUser = CatUsuarios.objects.get(usuario=userName)
    data = { 'userExist' : userVal , 'fullnameUser' : FullNameUser.nombre }
    #data = serializers.serialize("json", userVal)
    return JsonResponse(data, safe=False)

def grafica1(request):
    registros = Registros.objects.filter(status=True).only('valor', 'creado')[:400]
    data = serializers.serialize("json", registros)
    context = {'dataRegistros': data}
    return render(request, 'DistSocialApp/grafica1.html', context)

