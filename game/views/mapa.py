from django.shortcuts import render, redirect, get_object_or_404
from game.models import Referencia, Sobrevivente

def mapa(request):
    if request.user.is_authenticated:
        usuario = Sobrevivente.objects.get(usuario__id=request.user.id)
        outros = Sobrevivente.objects.exclude(id=usuario.id)
        referencias = Referencia.objects.all()
    return render(request, "theme/mapa.html", { "referencias" : referencias , "eu" : { "x": usuario.x, "y": usuario.y }, "outros" : outros  })

def novaRef(request, tipo, x, y):
    if request.user.is_authenticated:
        if tipo != 'Eu':
            Referencia.objects.create(x=x, y=y, tipo=tipo)
        else:
            usuario = Sobrevivente.objects.get(usuario__id=request.user.id)
            usuario.x = x
            usuario.y = y
            usuario.save()
    return redirect('mapa')