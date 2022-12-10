from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sobrevivente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuário")
    datenasc = models.DateField(verbose_name="Data de Nascimento")
    sexo_tipos = (
        ('M','Masculino'), 
        ('F','Feminino')
    )    
    sexo = models.CharField(verbose_name="Sexo", max_length=10, choices=sexo_tipos)
    saldo = models.IntegerField(verbose_name="Saldo", default=0)

    def __str__(self) -> str:
        return f"{self.usuario.first_name} {self.usuario.last_name} -> {self.saldo} pontos"

class Inventario(models.Model):
    sobrevivente = models.OneToOneField(Sobrevivente, on_delete=models.CASCADE, verbose_name="Dono")

    def __str__(self) -> str:
        return f" Inventário({self.id}) do sobrevivente {self.sobrevivente.nome}"

class Recurso(models.Model):
    descricao = models.CharField(verbose_name="Descrição", max_length=100)
    quantidade = models.IntegerField(verbose_name="Quantidade", default=1)
    validade = models.DateField(verbose_name="Validade", null=True, blank=True)
    recurso_tipos = (
        ('Ar', 'Água'),
        ('Al', 'Alimento'), 
        ('Ar', 'Arma'), 
        ('Mu', 'Munição'), 
        ('Tc', 'Tecnologia'), 
        ('Mp', 'Mapa'), 
        ('Ie', 'Item Especial')
    )
    tipo = models.CharField(verbose_name="Tipo", choices=recurso_tipos, max_length=2)
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE, verbose_name="Inventario")

    def __str__(self) -> str:
        return f"Item({self.id}) -> {self.descricao}"