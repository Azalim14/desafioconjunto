# Generated by Django 3.1.3 on 2021-03-09 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meta',
            name='semaforo',
            field=models.CharField(choices=[('verde', 'Verde'), ('amarelo', 'Amarelo'), ('vermelho', 'Vermelho')], default='verde', max_length=8),
            preserve_default=False,
        ),
    ]
