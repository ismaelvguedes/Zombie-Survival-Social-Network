from django.shortcuts import render, redirect
from game.models import Recurso

def inventario(request):
    if request.user.is_authenticated:
        recursos = Recurso.objects.all()
        return render(request, 'theme/inventario.html', { 'recursos' : recursos })
    return redirect('iniciar')