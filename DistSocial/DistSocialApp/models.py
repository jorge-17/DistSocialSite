from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class CatOrganizaciones(models.Model):
    id_CatOrganizacion = models.AutoField(primary_key=True)
    status = models.BooleanField(null=True)
    nombre = models.CharField(max_length=255, null=True)
    creado = models.DateTimeField(default=timezone.now, null=True)
    def __str__(self):
        return self.nombre

class CatTipos(models.Model):
    id_CatTipo = models.AutoField(primary_key=True)
    status = models.BooleanField(null=True)
    nombre = models.CharField(max_length=255, null=True)
    creado = models.DateTimeField(default=timezone.now, null=True)
    def __str__(self):
        return self.nombre

    def resYesterday(self):
        return self.creado >= timezone.now() - datetime.timedelta(days=1)

class CatUsuarios(models.Model):
    id_CatUsuario = models.AutoField(primary_key=True)
    status = models.BooleanField(null=True)
    usuario = models.CharField(max_length=255, null=True)
    pw = models.CharField(max_length=255, null=True)
    nombre = models.CharField(max_length=255, null=True)
    id_CatOrganizacion = models.ForeignKey(CatOrganizaciones, on_delete=models.CASCADE)
    creado = models.DateTimeField(default=timezone.now, null=True)
    
    def __str__(self):
        return self.nombre

class CatLocalidades(models.Model):
    id_CatLocalidad = models.AutoField(primary_key=True)
    status = models.BooleanField(null=True)
    nombre = models.CharField(max_length=255, null=True)
    latitud = models.DecimalField(max_digits=5, decimal_places=5, null=True)
    longitud = models.DecimalField(max_digits=5, decimal_places=5, null=True)
    id_CatOrganizacion = models.ForeignKey(CatOrganizaciones, on_delete=models.CASCADE)
    creado = models.DateTimeField(default=timezone.now, null=True)
    def __str__(self):
        return self.nombre

class CatCamaras(models.Model):
    id_CatCamara = models.AutoField(primary_key=True)
    status = models.BooleanField(null=True)
    nombre = models.CharField(max_length=255, null=True)
    ip = models.CharField(max_length=255, null=True)
    latitud = models.DecimalField(max_digits=5, decimal_places=5, null=True)
    longitud = models.DecimalField(max_digits=5, decimal_places=5, null=True)
    id_CatLocalidad = models.ForeignKey(CatLocalidades,on_delete=models.CASCADE)
    creado = models.DateTimeField(default=timezone.now, null=True)
    def __str__(self):
        return self.nombre

class Registros(models.Model):
    id_Registro = models.AutoField(primary_key=True)
    status = models.BooleanField(null=True)
    id_CatCamara = models.ForeignKey(CatCamaras, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=12, decimal_places=3, null=True)
    id_CatTipo = models.ForeignKey(CatTipos, on_delete=models.CASCADE)
    creado = models.DateTimeField(default=timezone.now, null=True)
    nombre = models.CharField(max_length=255, null=True)
    def getDateValue(self):
        return self.valor, self.creado

class CatDispositivos(models.Model):
    id_CatDispositivo = models.AutoField(primary_key=True)
    status = models.BooleanField(null=True)
    mac = models.CharField(null=True, max_length=255)
    creado = models.DateTimeField(default=timezone.now, null=True)

class Configuraciones(models.Model):
    id_Configuracion = models.AutoField(primary_key=True)
    status = models.BooleanField(null=True)
    nombre = models.CharField(null=True, max_length=100)
    valor =  models.CharField(null=True, max_length=100)
    tipo = models.CharField(null=True, max_length=10)


class Servers(models.Model):
    id_Server = models.AutoField(primary_key=True)
    status = models.BooleanField(null=True)
    nombre = models.CharField(null=True, max_length=100)
    puerto = models.IntegerField(null=True)
    user = models.CharField(null=True, max_length=100)
    pwd = models.CharField(null=True, max_length=100)
    nombre_db = models.CharField(null=True, max_length=100)    
    tipo = models.CharField(null=True, max_length=10)