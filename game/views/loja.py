from django.shortcuts import render, redirect, get_object_or_404
from game.models import Cambio, Oferta, Sobrevivente, Recurso, Inventario

def loja(request):
    if request.user.is_authenticated:
        ofertas = Oferta.objects.filter(concluida=False)
        return render(request, "theme/loja.html", { "ofertas" : ofertas, "quant": len(ofertas)  })
    return redirect('iniciar')

def minhasOfertas(request):
    if request.user.is_authenticated:
        vendedor = Sobrevivente.objects.get(id=request.user.id)
        ofertas = Oferta.objects.filter(vendedor__id=vendedor.id)
        return render(request, "theme/minhasOfertas.html", { "ofertas" : ofertas, "quant": len(ofertas)  })
    return redirect('iniciar')

def ofertar(request):
    if request.user.is_authenticated:
        id = request.GET.get("id", "")
        valor = int(request.GET.get("valor", ""))
        if (id is not None) and (valor is not None):
            produto = Recurso.objects.get(id=id)
            user = Sobrevivente.objects.get(id=request.user.id)
            if user.id == produto.inventario.sobrevivente.id:
                if produto.quantidade >= valor:
                    oferta = Oferta.objects.create(produto=produto, quantidade=valor, vendedor=user)
                    oferta.save()
                    return redirect('loja')
    return redirect('iniciar')

def detalharOferta(request, id):
    if request.user.is_authenticated: 
        usuario = Sobrevivente.objects.get(id=request.user.id)
        oferta = Oferta.objects.get(id=id)
        if oferta.vendedor == usuario:  
            cambios = Cambio.objects.filter(primaria__id=oferta.id)
            return render(request, "theme/detalharOferta.html", { "cambios" : cambios, "quant": len(cambios)  })
    
    return redirect('minhasOfertas')

def removerOferta(request, id):
    if request.user.is_authenticated: 
        usuario = Sobrevivente.objects.get(id=request.user.id)
        oferta = Oferta.objects.get(id=id)
        if oferta.vendedor == usuario:  
            oferta.delete()
            return redirect('minhasOfertas')
    
    return redirect('minhasOfertas')

def troca(primaria: Oferta, secundaria: Oferta, inv: int):
    if primaria.produto.quantidade > primaria.quantidade:
        primaria.produto.quantidade -= primaria.quantidade
        primaria.produto.save()
        Recurso.objects.create(
            inventario=Inventario.objects.get(id=inv), 
            descricao=primaria.produto.descricao, 
            quantidade=primaria.quantidade, 
            validade=primaria.produto.validade,
            tipo=primaria.produto.tipo
        )
    elif(primaria.produto.quantidade == primaria.quantidade):
        primaria.produto.inventario = Inventario.objects.get(id=inv)
        primaria.produto.save()

def aceitarCambio(request, id):
    if request.user.is_authenticated: 
        usuario = Sobrevivente.objects.get(id=request.user.id)
        cambio = Cambio.objects.get(id=id)
        if cambio.primaria.vendedor == usuario:  
            if not(cambio.primaria.concluida or cambio.secundaria.concluida) and (cambio.estado == 'E'):
                
                # Troca
                for cm in Cambio.objects.filter(primaria=cambio.primaria).exclude(id=cambio.id):
                    cm.estado = 'R'
                    cm.save()

                invPrim = int(cambio.primaria.produto.inventario.id)
                invSec = int(cambio.secundaria.produto.inventario.id)
                troca(cambio.primaria, cambio.secundaria, invSec)
                troca(cambio.secundaria, cambio.primaria, invPrim)

                # Configurações finais
                cambio.estado = 'A'
                cambio.primaria.concluida = True
                cambio.secundaria.concluida = True

                cambio.primaria.save()
                cambio.secundaria.save()
                cambio.save()
                
                return detalharOferta(request, cambio.primaria.id)

    return redirect('minhasOfertas')

def recusarCambio(request, id):
    if request.user.is_authenticated: 
        usuario = Sobrevivente.objects.get(id=request.user.id)
        cambio = Cambio.objects.get(id=id)
        if (cambio.primaria.vendedor == usuario) and (cambio.estado == 'E'):  
            cambio.estado = 'R'
            cambio.save()
            return detalharOferta(request, cambio.primaria.id)

    return redirect('minhasOfertas')

def selecionarOferta(request, id):
    if request.user.is_authenticated:
        comprador = Sobrevivente.objects.get(id=request.user.id)
        ofertas = Oferta.objects.filter(vendedor__id=comprador.id, concluida=False)
        if (id is not None): # id não veio vazio
            ofertaPrimaria = Oferta.objects.get(id=id)
            if ofertaPrimaria.vendedor != comprador:    
                return render(request, "theme/selecionarOfertas.html", { "ofertas" : ofertas, "id" : id, "quant": len(ofertas) })
            
    return redirect('loja')

def cambio(request, idP, idS):
    if request.user.is_authenticated:
        if (idP is not None) and (idS is not None):
            comprador = Sobrevivente.objects.get(id=request.user.id)
            ofp = Oferta.objects.get(id=idP) 
            ofs = Oferta.objects.get(id=idS)

            # Verifica se o quem colocou é realmente o dono secundario
            if ofs.vendedor == comprador: 

                # Verifica se quem ta ofertando não é a mesma pessoa
                if ofp.vendedor != comprador: 
                    
                    if not(ofp.concluida or ofs.concluida):
                        # Se ja existe um cambio para essas mesmas ofertas primaria e secundaria ou vice e versa
                        if (len(Cambio.objects.filter(primaria=ofp, secundaria=ofs))) + (len(Cambio.objects.filter(primaria=ofs, secundaria=ofp))) == 0:

                            if (ofp.produto.valor * ofp.quantidade) ==(ofs.produto.valor * ofs.quantidade):
                                Cambio.objects.create(primaria=ofp, secundaria=ofs, estado='E')
                                return redirect('meusCambios')

    return redirect('loja')

def removerCambio(request, id):
    if request.user.is_authenticated: 
        usuario = Sobrevivente.objects.get(id=request.user.id)
        cambio = Cambio.objects.get(id=id)
        if cambio.secundaria.vendedor == usuario:  
            cambio.delete()
            return redirect('meusCambios')
    
    return redirect('meusCambios')

def meusCambios(request):
    if request.user.is_authenticated:
        usuario = Sobrevivente.objects.get(id=request.user.id)
        ofertas = Oferta.objects.filter(vendedor__id=usuario.id)
        cambios = []
        for oferta in ofertas:
            cs = Cambio.objects.filter(secundaria__id=oferta.id)
            for c in cs:
                cambios.append(c)
        return render(request, "theme/meusCambios.html", { "cambios" : cambios, "quant": len(cambios)  })
    return redirect('iniciar')