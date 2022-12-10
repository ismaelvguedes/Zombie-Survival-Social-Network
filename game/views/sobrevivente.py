from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from game.models import Sobrevivente

def iniciar(request):
    return render(request, 'theme/inicio.html')

def conectar(request):
    return render(request, 'theme/entrada.html')

def desconectar(request):
    logout(request)
    return redirect('iniciar')

def autenticar(request):
    usuario = request.POST['user']
    senha = request.POST['pass']
    sobrevivente = authenticate(request, username=usuario, password=senha)
    if sobrevivente is not None:
        login(request, sobrevivente)
        return redirect('iniciar')
    else:
        return redirect('conectar')

def listar_sobreviventes(request):
    sobreviventes = Sobrevivente.objects.all()
    return render(request, 'theme/listar.html', { 'sobreviventes' : sobreviventes})