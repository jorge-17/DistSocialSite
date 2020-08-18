from django.urls import path
from . import views

app_name = 'DistSocial'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('camaras/', views.camaras, name='camaras'),
    path('localidades/', views.localidades, name='localidades'),
    path('grafica1/', views.grafica1,  name='grafica1')
]