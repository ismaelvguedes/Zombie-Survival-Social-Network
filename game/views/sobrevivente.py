from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from game.forms import UsuarioCreateForm, SobreviventeForm
from game.models import Sobrevivente, Inventario

def iniciar(request):
    return render(request, 'theme/inicio.html')

def conectar(request):
    return render(request, 'theme/entrada.html')

def cadastrar(request):
    if request.method == "POST":
        formUser = UsuarioCreateForm(request.POST)
        formSob = SobreviventeForm(request.POST)
        
        if formUser.is_valid() and formSob.is_valid():
            usuario = formUser.save()
            sobrevivente = formSob.save(commit=False)
            sobrevivente.usuario = usuario
            formSob.save()
            inventario = Inventario.objects.create(sobrevivente=sobrevivente)
            inventario.save()

            return redirect('iniciar')

    else:
        formUser = UsuarioCreateForm()
        formSob = SobreviventeForm()

    return render(request, 'theme/cadastrar.html', { 'formUser' : formUser, 'formSob' : formSob })

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