from django.shortcuts import render, redirect, get_object_or_404
from game.models import Cambio, Oferta

def loja(request):
    ofertas = Oferta.objects.all()
    return render(request, "theme/loja.html", { "ofertas" : ofertas })