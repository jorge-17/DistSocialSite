from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader, RequestContext, Template, Context
from django.core import serializers
from django.shortcuts import get_object_or_404, render
from .models import CatCamaras, CatLocalidades, CatUsuarios, CatOrganizaciones, Registros, CatDispositivos, Configuraciones, Servers


# Create your views here.
def index(request):    
    lista_organizaciones = CatOrganizaciones.objects.order_by('id_CatOrganizacion')
    context = {'lista_org' : lista_organizaciones}
    return render(request, 'DistSocialApp/index.html', context)

def tablaLocalidades(request):
    lista_localidades = CatLocalidades.objects.order_by('id_CatLocalidad')[:15]
    context = {'lista_localidades': lista_localidades}    
    return render(request, 'DistSocialApp/localidades.html', context)

def tablaCamaras(request):
    lista_camaras = CatCamaras.objects.order_by('id_CatCamara')[:15]
    context = {'lista_camaras': lista_camaras}
    return render(request, 'DistSocialApp/camaras.html', context)

def login(request):
    userName = request.POST.get('userName')
    userPass = request.POST.get('userPass')
    userVal = CatUsuarios.objects.filter(usuario=userName, pw=userPass).exists()    
    FullNameUser = CatUsuarios.objects.get(usuario=userName)
    idOrganizacion = str(FullNameUser.id_CatOrganizacion)
    data = { 'userExist' : userVal , 'fullnameUser' : FullNameUser.nombre , 'idOrganizacion': idOrganizacion}
    return JsonResponse(data, safe=False)

def home(request):
    numRegistros = Registros.objects.count()
    numLocalidades = CatLocalidades.objects.count()
    numCamaras = CatCamaras.objects.count()
    context = {'numRegistros': numRegistros, 'numLocalidades': numLocalidades, 'numCamaras': numCamaras}
    return render(request, 'DistSocialApp/home.html', context)

def graficaHistorica(request):
    registros = Registros.objects.filter(status=True).order_by('-id_Registro').only('valor', 'creado')[:400]
    lista_localidades = CatLocalidades.objects.order_by('id_CatLocalidad')[:15]
    data = serializers.serialize("json", registros)
    context = {'dataRegistros': data, 'listaLocalidades': lista_localidades}
    return render(request, 'DistSocialApp/grafica1.html', context)

def ListCamaras(request, idLocalidad):
    listaCamaras = CatCamaras.objects.filter(id_CatLocalidad=idLocalidad).order_by('id_CatCamara')
    context = {'lista_camaras': listaCamaras}
    return render(request, 'DistSocialApp/camaras.html', context)


def filtroGrafica(request, idCamara):
    listaRegistros = Registros.objects.filter(id_CatCamara=idCamara, status=True).order_by('-id_Registro').only('valor', 'creado')
    infoCamara = CatCamaras.objects.get(id_CatCamara = idCamara)
    data = serializers.serialize("json", listaRegistros)
    context = {'dataRegistros': data, 'infoCamara': infoCamara}
    return render(request, 'DistSocialApp/graficaFiltro.html', context)


def formConfigRemote(request):
    listaConfigDB = Servers.objects.filter(tipo='bd')
    listaConfigMQTT = Servers.objects.filter(tipo='mqtt')
    context = {'lista_config_db': listaConfigDB, 'lista_config_mqtt': listaConfigMQTT}
    return render(request, 'DistSocialApp/formConfig.html', context)

def saveConfig(request):
    idServer = request.POST.get('idServer')
    server_name = request.POST.get('server_name')
    port = request.POST.get('port')
    user = request.POST.get('user')
    pwd = request.POST.get('pass')
    database_name = request.POST.get('database_name')
    tipo = request.POST.get('tipo')

    server_name_query = Servers.objects.filter(id_Server=idServer).update(nombre=server_name, puerto=port, user=user, pwd=pwd, nombre_db=database_name, tipo=tipo)
    server_name_query.save()    

    listaConfigDB = Servers.objects.get(tipo='bd')
    listaConfigMQTT = Servers.objects.get(tipo='mqtt')
    context = {'lista_config_db': listaConfigDB, 'lista_config_mqtt': listaConfigMQTT}
    return render(request, 'DistSocialApp/formConfig.html', context)