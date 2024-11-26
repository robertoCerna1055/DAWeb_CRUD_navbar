# Generated by Django 5.1.1 on 2024-11-23 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id_cliente', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre_cliente', models.CharField(max_length=45)),
                ('apellido_P', models.CharField(max_length=45)),
                ('apellido_M', models.CharField(max_length=45)),
                ('fecha_de_nacimiento', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=15)),
                ('genero', models.CharField(max_length=9)),
            ],
        ),
    ]
