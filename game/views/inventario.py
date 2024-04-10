from django.shortcuts import render, redirect, get_object_or_404
from game.models import Sobrevivente, Inventario, Recurso
from game.forms import RecursoForm

def inventario(request):
    if request.user.is_authenticated:
        recursos = Recurso.objects.filter(inventario=Inventario.objects.get(sobrevivente__id=Sobrevivente.objects.get(id=request.user.id).id))
        quant = len(recursos)
        return render(request, 'theme/inventario.html', { 'recursos' : recursos , 'quant': quant})
    return redirect('iniciar')

def adicionarRecurso(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            formRec = RecursoForm(request.POST)

            if formRec.is_valid():
                recurso = formRec.save(commit=False)
                recurso.inventario = Inventario.objects.get(sobrevivente__id=Sobrevivente.objects.get(id=request.user.id).id)
                formRec.save()
                return redirect('inventario')

        else:
            formRec = RecursoForm()

        return render(request, 'theme/adicionarRecurso.html', { 'formRec' : formRec })
    
    return redirect('iniciar')

def editarRecurso(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            formRec = RecursoForm(request.POST)

            if formRec.is_valid():
                recurso = get_object_or_404(Recurso, pk=id)
                novo = formRec.save(commit=False)
                recurso.descricao = novo.descricao
                recurso.quantidade = novo.quantidade
                recurso.validade = novo.validade
                recurso.tipo = novo.tipo
                recurso.save()
                return redirect('inventario')

                # recurso.inventario = Inventario.objects.get(sobrevivente__id=Sobrevivente.objects.get(usuario__id=request.user.id).id)
        recurso = get_object_or_404(Recurso, pk=id)
        formRec = RecursoForm(instance=recurso)
        return render(request, 'theme/editarRecurso.html', { 'idr' : id, 'formRec' : formRec })

    return redirect('iniciar')

def removerRecurso(request, id):
    if request.user.is_authenticated: 
        recurso = get_object_or_404(Recurso, pk=id)      
        recurso.delete()
        return redirect('inventario')
    
    return redirect('iniciar')