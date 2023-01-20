from django.urls import path
from game.views.sobrevivente import *
from game.views.inventario import *
from game.views.loja import *
from game.views.mapa import *
from game.views.chat import *

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

    # Loja:
    path('loja', loja, name="loja"),
    path('ofertar', ofertar, name="ofertar"),
    path('minhas_ofertas', minhasOfertas, name="minhasOfertas"),
    path('minhas_ofertas/<int:id>/detalhar', detalharOferta, name="detalharOferta"),
    path('minhas_ofertas/<int:id>/deletar', removerOferta, name="removerOferta"),
    path('minhas_ofertas/<int:id>/aceitar', aceitarCambio, name="aceitarCambio"),
    path('minhas_ofertas/<int:id>/recusar', recusarCambio, name="recusarCambio"),

    # Cambio:
    path('meus_cambios', meusCambios, name="meusCambios"),
    path('cambio/<int:id>/novo', selecionarOferta, name="cambio"),
    path('cambio/<int:idS>/<int:idP>/confirmar', cambio, name="cambio"),
    path('cambio/<int:id>/deletar', removerCambio, name="removerCambio"),

    # Mapa:
    path('mapa', mapa, name="mapa"),
    path('mapa/<str:tipo>/<int:x>/<int:y>/novo', novaRef, name="novaRef"),

    # Chat:
    path('chat/sobreviventes', listarSobre, name="sobreviventes"),
    path('chat/<int:id>/abrir', chat, name="chat"),
    path('chat/<int:id>/enviar', enviar, name="enviar"),
    path('chat/<int:id>/denunciar', denunciar, name="denunciar"),
]