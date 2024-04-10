from django import forms
from game.models import Sobrevivente, Recurso

# class UsuarioCreateForm(UserCreationForm):

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'first_name', 'last_name')

class SobreviventeForm(forms.ModelForm):
    class Meta:
        model = Sobrevivente
        fields = ('nomeCompleto', 'sexo', 'datenasc', 'email', 'password')
        widgets = {
            'datenasc': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'password': forms.PasswordInput(render_value=True),
        }

class RecursoForm(forms.ModelForm):

    class Meta:
        model = Recurso
        fields = ('descricao', 'quantidade', 'validade', 'valor', 'tipo')
        widgets = {
            'validade': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }