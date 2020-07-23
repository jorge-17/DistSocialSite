from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/camaras/', views.camaras, name='camaras'),
    path('/localidades/', views.localidades, name='localidades')
]