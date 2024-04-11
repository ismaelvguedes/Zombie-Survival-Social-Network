from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
class Sobrevivente(AbstractUser):
    username = None
    first_name = None
    last_name = None

    nomeCompleto = models.CharField(max_length=100, verbose_name="Nome completo")
    email = models.EmailField(unique=True)
    x = models.IntegerField(verbose_name="x", default=0)
    y = models.IntegerField(verbose_name="y", default=0)
    datenasc = models.DateField(verbose_name="Data de Nascimento")
    sexo_tipos = (('M','Masculino'), ('F','Feminino'))    
    sexo = models.CharField(verbose_name="Sexo", max_length=10, choices=sexo_tipos)

    xp = models.IntegerField(verbose_name="XP", default=0)
    denuncias = models.IntegerField(verbose_name="Denuncias", default=0)
    infectado = models.BooleanField(verbose_name="Infectado", default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nomeCompleto','datenasc','sexo',]

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Sobrevivente"
        verbose_name_plural = "Sobreviventes"

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Inventario(models.Model):
    sobrevivente = models.OneToOneField(Sobrevivente, on_delete=models.CASCADE, verbose_name="Dono")

    def __str__(self) -> str:
        return f" Inventário de {self.sobrevivente.email}"

class Recurso(models.Model):
    descricao = models.CharField(verbose_name="Descricao", max_length=100)
    quantidade = models.IntegerField(verbose_name="Quantidade", default=1)
    validade = models.DateField(verbose_name="Validade", null=True, blank=True, help_text="Somente se for perecível")
    recurso_tipos = (
        ('Ar', 'Agua'),
        ('Al', 'Alimento'), 
        ('Ar', 'Arma'), 
        ('Mu', 'Municao'), 
        ('Tc', 'Tecnologia'), 
        ('Mp', 'Mapa'), 
        ('Ie', 'Item Especial')
    )
    tipo = models.CharField(verbose_name="Tipo", choices=recurso_tipos, max_length=2)
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE, verbose_name="Inventario")
    valor = models.IntegerField(verbose_name="Valor", default=0)

    def __str__(self) -> str:
        return f"{self.descricao}"

    def verTipo(self) -> str:
        for valor in self.recurso_tipos: 
            if valor[0] == self.tipo:
                return valor[1]

class Oferta(models.Model):
    produto = models.ForeignKey(Recurso, on_delete=models.CASCADE, verbose_name="Oferta")
    quantidade = models.IntegerField(verbose_name="Quantidade", default=1)
    vendedor = models.ForeignKey(Sobrevivente, on_delete=models.CASCADE, verbose_name="Dono")
    concluida = models.BooleanField(verbose_name="Concluida", default=False)

    def __str__(self) -> str:
        return f'{self.produto}'

class Cambio(models.Model):
    primaria = models.ForeignKey(Oferta, on_delete=models.CASCADE, related_name="oferta_primaria")
    secundaria = models.ForeignKey(Oferta, on_delete=models.CASCADE, related_name="oferta_secundaria")
    estados = (
        ('E', 'Espera'),
        ('A', 'Aceito'), 
        ('R', 'Recusado'), 
    )
    estado = models.CharField(verbose_name="Estado", choices=estados, max_length=10)
    
    def __str__(self) -> str:
        return f'Cambio({self.id})'

    def verEstado(self):
        for posicao in self.estados:
            if self.estado == posicao[0]:
                return posicao[1]

class Referencia(models.Model):
    x = models.IntegerField(verbose_name="x", default=0)
    y = models.IntegerField(verbose_name="y", default=0)
    tipos = (
        ('Or', 'Orda'),
        ('Fz', 'Fazenda'),
        ('Md', 'Mercado'),
        ('Ht', 'Hotel'),
        ('Ae', 'Aeroporto'),
        ('Pt', 'Porto'),
        ('Qt', 'Quartel'),
    )
    tipo = models.CharField(verbose_name="Tipo", choices=tipos, max_length=10)

    def __str__(self) -> str:
        return f'{self.tipo} - x: { self.x } ; y: { self.y }'

    def verTipo(self):
        for posicao in self.tipos:
            if self.tipo == posicao[0]:
                return posicao[1]

class Mensagem(models.Model):
    emissor = models.ForeignKey(Sobrevivente, on_delete=models.CASCADE, verbose_name="Emissor", related_name="emissor")
    receptor = models.ForeignKey(Sobrevivente, on_delete=models.CASCADE, verbose_name="Receptor", related_name="receptor")
    msg = models.TextField(max_length="300", verbose_name="Mensagem")
    tempo = models.DateTimeField(auto_now=True, verbose_name="Tempo")

    def __str__(self) -> str:
        return f"Msg({self.id}) de {self.emissor} para {self.receptor}"
    
    class Meta:
        verbose_name = "Mensagem"
        verbose_name_plural = "Mensagens"
