from django.shortcuts import render, redirect, get_object_or_404
from game.models import Sobrevivente, Inventario, Recurso
from game.forms import RecursoForm

def inventario(request):
    if request.user.is_authenticated:
        recursos = Recurso.objects.filter(inventario=Inventario.objects.get(sobrevivente__id=Sobrevivente.objects.get(usuario__id=request.user.id).id))
        return render(request, 'theme/inventario.html', { 'recursos' : recursos })
    return redirect('iniciar')

def adicionarRecurso(request):
    if request.method == "POST":
        formRec = RecursoForm(request.POST)

        if formRec.is_valid():
            recurso = formRec.save(commit=False)
            recurso.inventario = Inventario.objects.get(sobrevivente__id=Sobrevivente.objects.get(usuario__id=request.user.id).id)
            formRec.save()
            return redirect('inventario')

    else:
        formRec = RecursoForm()

    return render(request, 'theme/adicionarRecurso.html', { 'formRec' : formRec })

def removerRecurso(request, id):
    if request.user.is_authenticated: 
        recurso = get_object_or_404(Recurso, pk=id)      
        recurso.delete()
        return redirect('inventario')