from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from game.forms import SobreviventeForm
from game.models import Sobrevivente, Inventario

def iniciar(request):
    return render(request, 'theme/inicio.html')

def conectar(request):
    return render(request, 'theme/entrada.html')

def cadastrar(request):
    if request.method == "POST":
        formSob = SobreviventeForm(request.POST)
        
        if formSob.is_valid():
            sobrevivente = formSob.save(commit=False)
            formSob.save()
            inventario = Inventario.objects.create(sobrevivente=sobrevivente)
            inventario.save()

            return redirect('iniciar')

    else:
        formSob = SobreviventeForm()

    return render(request, 'theme/cadastrar.html', { 'formSob' : formSob })

def desconectar(request):
    logout(request)
    return redirect('iniciar')

def autenticar(request):
    email = request.POST['email']
    senha = request.POST['pass']
    sobrevivente = authenticate(request, email=email, password=senha)
    if sobrevivente is not None:
        login(request, sobrevivente)
        return redirect('iniciar')
    else:
        return redirect('conectar')


def listar_sobreviventes(request):
    sobreviventes = Sobrevivente.objects.all()
    return render(request, 'theme/listar_sobreviventes.html', { 'sobreviventes' : sobreviventes})