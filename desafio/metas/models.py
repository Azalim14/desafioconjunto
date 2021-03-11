from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

STATUS = (
    ('doing', 'Doing'),
    ('done', 'Done')
)

COR = (
    ('verde', 'Verde'),
    ('amarelo', 'Amarelo'),
    ('vermelho', 'Vermelho'),
    ('azul', 'Azul'),
    ('cinza', 'Cinza')
)

class Setor(models.Model):
    name = models.CharField(max_length = 50)
    ident = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name

class Membro(models.Model):
    name = models.CharField(max_length = 25)
    setor = models.ForeignKey(Setor, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Meta(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    done = models.CharField(max_length=5, choices=STATUS)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    setor = models.ForeignKey(Setor, on_delete = models.CASCADE)
    responsavel = models.ForeignKey(Membro, on_delete = models.CASCADE)
    membros = models.CharField(max_length = 250)
    entrega = models.DateField()
    deletado = models.BooleanField()
    porcentagem = models.IntegerField()
    semaforo = models.CharField(max_length=8, choices=COR)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    fk_meta = models.ForeignKey(Meta, on_delete = models.CASCADE)
    usuario = models.ForeignKey(Membro, on_delete=models.CASCADE)
    oquefoifeito = models.TextField(max_length = 255)
    oquevaiserfeito = models.TextField(max_length = 255, blank = True)
    impedimento = models.TextField(max_length = 255, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fk_meta.titulo + " | " +self.usuario.name + " | " + str(self.created_at)