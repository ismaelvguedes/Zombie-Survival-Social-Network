from django.shortcuts import render, redirect, get_object_or_404
from game.models import Mensagem, Sobrevivente

def listarSobre(request):
    if request.user.is_authenticated:
        usuario = Sobrevivente.objects.get(usuario__id=request.user.id)
        sobreviventes = Sobrevivente.objects.exclude(id=usuario.id)
        return render(request, "theme/listarSobreviventes.html", { "sobreviventes" : sobreviventes})
    return redirect('iniciar')

def chat(request, id):
    if request.user.is_authenticated:
        emissor = Sobrevivente.objects.get(usuario__id=request.user.id)
        receptor = get_object_or_404(Sobrevivente, pk=id)
        mensagens = Mensagem.objects.filter(emissor=emissor, receptor=receptor)
        mensagens_inv = Mensagem.objects.filter(emissor=receptor, receptor=emissor)
        msg = mensagens.union(mensagens_inv).order_by("tempo")
        return render(request, "theme/chat.html", { "mensagens" : msg, "receptor" : receptor, "emissor" : emissor })
    return redirect('iniciar')

def enviar(request, id):
    if request.user.is_authenticated:
        emissor = Sobrevivente.objects.get(usuario__id=request.user.id)
        receptor = get_object_or_404(Sobrevivente, pk=id)
        msg = request.POST['mensagem']
        if msg != '':
            mensagem = Mensagem.objects.create(emissor=emissor, receptor=receptor, msg=msg)
            mensagem.save()

        return redirect('chat', id)
    return redirect('iniciar')