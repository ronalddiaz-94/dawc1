# Generated by Django 4.0.6 on 2022-08-18 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carreras', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carrera',
            options={'ordering': ['-nameCarrer'], 'verbose_name': 'FACULTAD CIENCIA E INGENIERIA', 'verbose_name_plural': 'Lista de carreras'},
        ),
    ]
