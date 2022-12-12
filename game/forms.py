from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from game.models import Sobrevivente, Recurso

class DateInput(forms.DateInput):
    input_type = 'date'

class UsuarioCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class SobreviventeForm(forms.ModelForm):

    datenasc = forms.DateField(widget=DateInput(), label='Data de Nascimento')
    
    class Meta:
        model = Sobrevivente
        fields = ('datenasc', 'sexo')

class RecursoForm(forms.ModelForm):

    validade = forms.DateField(widget=DateInput())

    class Meta:
        model = Recurso
        fields = ('descricao', 'quantidade', 'validade', 'tipo')