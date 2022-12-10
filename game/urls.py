from django.urls import path
from game.views.sobrevivente import *

urlpatterns = [
    path('conectar', conectar, name="conectar"),
    path('desconectar', desconectar, name="desconectar"),
    path('autenticar', autenticar, name="autenticar"),
    path('listar', listar_sobreviventes, name="inicio"),
]