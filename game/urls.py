from django.urls import path
from game.views.sobrevivente import *
from game.views.inventario import *
from game.views.loja import *

urlpatterns = [
    
    path('', iniciar, name="iniciar"), # home

    # Sobrevivente:
    path('conectar', conectar, name="conectar"),
    path('cadastrar', cadastrar, name="cadastrar"),
    path('desconectar', desconectar, name="desconectar"),
    path('autenticar', autenticar, name="autenticar"),
    path('listar_sobreviventes', listar_sobreviventes, name="listar"),

    # Recurso:
    path('inventario', inventario, name="inventario"),
    path('inventario/novo', adicionarRecurso, name="adicionarRecurso"),
    path('inventario/<int:id>/editar', editarRecurso, name="editarRecurso"),
    path('inventario/<int:id>/deletar', removerRecurso, name="removerRecurso"),

    # Loja
    path('loja', loja, name="loja"),
]