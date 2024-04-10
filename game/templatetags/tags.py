from django import template 
from django.conf import settings
from game.models import Sobrevivente
register = template.Library() 

@register.simple_tag
def tipoUser(id):
    infectado = Sobrevivente.objects.get(id=id).infectado
    sexo = Sobrevivente.objects.get(id=id).sexo

    if infectado:
        return  settings.STATIC_URL + "img/icone-infectado.png"
    else:
        if sexo == 'F':
            return settings.STATIC_URL + "img/icone-alex.png"
        else:
            return settings.STATIC_URL + "img/icone-steve.png"