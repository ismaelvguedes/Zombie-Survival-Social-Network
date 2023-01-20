from rest_framework import serializers
from game.models import *
from django.contrib.auth.models import User

class SobreviventeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sobrevivente
        fields = '__all__'

class RecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recurso
        fields = '__all__'

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        write_only_fields = ('password',)
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class OfertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oferta
        fields = '__all__'

class CambioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cambio
        fields = '__all__'