from django.urls import path
from game.views.sobrevivente import *

urlpatterns = [
    path('listar', listar_sobreviventes, name="listar"),
]
