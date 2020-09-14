from django.urls import path
from . import views

app_name = 'DistSocial'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('camaras/', views.tablaCamaras, name='camaras'),
    path('localidades/', views.tablaLocalidades, name='localidades'),
    path('graficaH/', views.graficaHistorica,  name='graficaH'),
    path('<int:idLocalidad>/', views.ListCamaras, name='ListCamaras'),
    path('filtroGrafica/<int:idCamara>/', views.filtroGrafica, name="filtroGrafica"),
    path('formConfigRemote/', views.formConfigRemote, name="formConfigRemote"),
    path('saveConfig/', views.saveConfig, name="saveConfig")
]