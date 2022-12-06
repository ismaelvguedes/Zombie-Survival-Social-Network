from django.shortcuts import render, redirect
from game.models import Sobrevivente

def listar_sobreviventes(request):
    sobreviventes = Sobrevivente.objects.all()
    return render(request, 'theme/listar.html', { 'sobreviventes' : sobreviventes})