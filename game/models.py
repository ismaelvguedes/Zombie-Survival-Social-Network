from django.db import models

# Create your models here.
class Sobrevivente(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=30)
    idade = models.IntegerField(verbose_name="Idade")
    sexo_tipos = ('Masculino', 'Feminino')    
    sexo = models.CharField(verbose_name="Sexo", max_length=10, choices=sexo_tipos)
    saldo = models.IntegerField(verbose_name="Saldo")

    def __str__(self) -> str:
        return f"{self.nome} -> {self.saldo} pontos"

class Inventario(models.Model):
    sobrevivente = models.OneToOneField(Sobrevivente, on_delete=models.CASCADE, verbose_name="Dono")

    def __str__(self) -> str:
        return f" Inventário({self.id}) do sobrevivente {self.sobrevivente.nome}"

class Recurso(models.Model):
    descricao = models.CharField(verbose_name="Descrição", max_length=100)
    quantidade = models.IntegerField(verbose_name="Quantidade")
    validade = models.DateField(verbose_name="Validade", null=True, blank=True)
    recurso_tipos = ('Água','Alimento', 'Arma', 'Munição', 'Tecnologia', 'Mapa', 'Item Especial')
    tipo = models.CharField(verbose_name="Tipo", choices=recurso_tipos)
    inventario = models.OneToOneField(Inventario, on_delete=models.CASCADE, verbose_name="Inventario")

    def __str__(self) -> str:
        return f"Item({self.id}) -> {self.descricao}"