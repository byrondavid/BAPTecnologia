# Generated by Django 3.0.4 on 2020-04-04 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='ver_en_web',
            field=models.BooleanField(default=True),
        ),
    ]
