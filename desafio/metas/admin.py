from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Meta)
admin.site.register(models.Comentario)
admin.site.register(models.Setor)
admin.site.register(models.Membro)
