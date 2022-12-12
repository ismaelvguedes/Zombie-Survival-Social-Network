from django.urls import path
from game.views.sobrevivente import *
from game.views.recurso import *

urlpatterns = [
    
    path('', iniciar, name="iniciar"), # home

    # Sobrevivente:
    path('conectar', conectar, name="conectar"),
    path('cadastrar', cadastrar, name="cadastrar"),
    path('desconectar', desconectar, name="desconectar"),
    path('autenticar', autenticar, name="autenticar"),
    path('listar_sobreviventes', listar_sobreviventes, name="listar"),

     # Recurso:
     path('listar_recursos', listar_recursos, name="listar_recursos"),

]