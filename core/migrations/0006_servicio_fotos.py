# Generated by Django 3.0.4 on 2020-04-04 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_cliente_fotos'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='fotos',
            field=models.ManyToManyField(to='core.Foto'),
        ),
    ]
