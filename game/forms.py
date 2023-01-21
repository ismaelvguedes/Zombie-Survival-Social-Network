from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from game.models import Sobrevivente, Recurso

class UsuarioCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class SobreviventeForm(forms.ModelForm):

    class Meta:
        model = Sobrevivente
        fields = ('datenasc', 'sexo')
        widgets = {
            'datenasc': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
        }

class RecursoForm(forms.ModelForm):

    class Meta:
        model = Recurso
        fields = ('descricao', 'quantidade', 'validade', 'valor', 'tipo')
        widgets = {
            'validade': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
        }