# Generated by Django 2.1 on 2020-03-21 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pesaje',
            fields=[
                ('ticket', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('peso', models.CharField(max_length=30)),
                ('placa', models.CharField(max_length=10)),
                ('fecha_ingreso', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
