# Generated by Django 4.1.7 on 2023-05-11 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cronograma', '0002_materia_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='cpf',
            field=models.CharField(help_text='CPF do professor', max_length=14, verbose_name='CPF'),
        ),
    ]
