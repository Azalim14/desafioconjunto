from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

STATUS = (
    ('doing', 'Doing'),
    ('done', 'Done')
)

class Setor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Meta(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(max_length=5, choices=STATUS)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    fk_setor = models.ForeignKey(Setor, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

class Comentario(models.Model):
    fk_meta = models.ForeignKey(Meta, on_delete = models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
