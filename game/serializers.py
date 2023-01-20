from rest_framework import serializers
from game.models import Sobrevivente

class SobreviventeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sobrevivente
        fields = '__all__'