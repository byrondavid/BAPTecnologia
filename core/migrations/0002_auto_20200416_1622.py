# Generated by Django 3.0.4 on 2020-04-16 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fotoproducto',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='fotoproducto',
            name='titulo',
        ),
        migrations.RemoveField(
            model_name='fotoproducto',
            name='ver_en_web',
        ),
        migrations.RemoveField(
            model_name='fotoseguimiento',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='fotoseguimiento',
            name='titulo',
        ),
        migrations.RemoveField(
            model_name='fotoseguimiento',
            name='ver_en_web',
        ),
        migrations.RemoveField(
            model_name='fotoservicio',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='fotoservicio',
            name='titulo',
        ),
        migrations.RemoveField(
            model_name='fotoservicio',
            name='ver_en_web',
        ),
    ]