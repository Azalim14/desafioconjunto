from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

STATUS = (
    ('doing', 'Doing'),
    ('done', 'Done')
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
    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(max_length=5, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    setor = models.ForeignKey(Setor, on_delete = models.CASCADE)
    responsavel = models.ForeignKey(Membro, on_delete = models.CASCADE)
    membros = models.CharField(max_length = 250)
    entrega = models.DateField()

    def __str__(self):
        return self.title

class Comentario(models.Model):
    fk_meta = models.ForeignKey(Meta, on_delete = models.CASCADE)
    user = models.ForeignKey(Membro, on_delete=models.CASCADE)
    oquefoifeito = models.CharField(max_length = 255)
    oquevaiserfeito = models.CharField(max_length = 255, blank = True)
    impedimento = models.CharField(max_length = 255, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
