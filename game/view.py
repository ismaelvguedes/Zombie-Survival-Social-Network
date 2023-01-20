from rest_framework import viewsets, filters
from game.serializers import SobreviventeSerializer
from game.models import Sobrevivente
from django_filters.rest_framework import DjangoFilterBackend

class SobreviventeViewSet(viewsets.ModelViewSet):
    """Listando sobreviventes"""
    queryset = Sobrevivente.objects.all()
    serializer_class = SobreviventeSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering = ['usuario__first_name']
    search_fields = ['usuario_first_name']
    filterset_fields = ['infectado']