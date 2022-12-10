from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from game.models import Sobrevivente

class DateInput(forms.DateInput):
    input_type = 'date'

class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name' , 'last_name', 'email')

class SobreviventeForm(forms.ModelForm):
    datenasc = forms.DateField(widget=DateInput(), label='Data de Nascimento')
    
    class Meta:
        model = Sobrevivente
        fields = ('datenasc', 'sexo')