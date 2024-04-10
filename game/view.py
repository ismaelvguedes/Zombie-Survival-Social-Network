from rest_framework import viewsets, filters
from game.serializers import *
from game.models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# class SobreviventeViewSet(viewsets.ModelViewSet):
#     """Listando sobreviventes"""
#     queryset = Sobrevivente.objects.all()
#     serializer_class = SobreviventeSerializer
#     # permission_classes = (IsAuthenticatedOrReadOnly,)
#     filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
#     search_fields = ['infectado']
#     filterset_fields = ['infectado']

# class RecursoViewSet(viewsets.ModelViewSet):
#     """Listando recursos"""
#     queryset = Recurso.objects.all()
#     serializer_class = RecursoSerializer
#     # permission_classes = (IsAuthenticatedOrReadOnly,)
#     filter_backends = [DjangoFilterBackend, filters.OrderingFilter]

# class InventarioViewSet(viewsets.ModelViewSet):
#     """Listando inventarios"""
#     queryset = Inventario.objects.all()
#     serializer_class = InventarioSerializer

# class OfertaViewSet(viewsets.ModelViewSet):
#     """Listando Ofertas"""
#     queryset = Oferta.objects.all()
#     serializer_class = OfertaSerializer    

# class CambioViewSet(viewsets.ModelViewSet):
#     """Listando Cambios"""
#     queryset = Cambio.objects.all()
#     serializer_class = CambioSerializer    