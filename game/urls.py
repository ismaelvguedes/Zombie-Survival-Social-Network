from django.urls import path
from game.views.sobrevivente import *

urlpatterns = [
    path('', iniciar, name="iniciar"),
    path('conectar', conectar, name="conectar"),
    path('cadastrar', cadastrar, name="cadastrar"),
    path('desconectar', desconectar, name="desconectar"),
    path('autenticar', autenticar, name="autenticar"),
    path('listar', listar_sobreviventes, name="listar"),
]