from django.urls import path
from django.contrib.auth import views as auth_views

from textos.views import  Mision, Vision, Valores,PoliCal


urlpatterns = [

    path('mision/',Mision.as_view(), name='mision'),
    path('vision/',Vision.as_view(), name='vision'),
    path('valores/',Valores.as_view(), name='valores'),
    path('politica_calidad/',PoliCal.as_view(), name='politica_calidad'),
 
]