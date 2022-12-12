from django.shortcuts import render, redirect
from game.models import Recurso

def listar_recursos(request):
    if request.user.is_authenticated:
        recursos = Recurso.objects.all()
        return render(request, 'theme/listar_recursos.html', { 'recursos' : recursos })
    return redirect('iniciar')