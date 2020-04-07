# Generated by Django 2.1 on 2020-03-31 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pesaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso_neto', models.DecimalField(decimal_places=3, max_digits=8)),
                ('peso_salida', models.DecimalField(decimal_places=3, max_digits=8)),
                ('peso_ingreso', models.DecimalField(decimal_places=3, max_digits=8)),
                ('placa', models.CharField(max_length=12)),
                ('fecha_ingreso', models.DateField(auto_now_add=True)),
                ('fecha_salida', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PesajeExterno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso_neto', models.DecimalField(decimal_places=3, max_digits=8)),
                ('peso_salida', models.DecimalField(decimal_places=3, max_digits=8)),
                ('peso_ingreso', models.DecimalField(decimal_places=3, max_digits=8)),
                ('placa', models.CharField(max_length=12)),
                ('fecha_ingreso', models.DateField(auto_now_add=True)),
                ('fecha_salida', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=12)),
                ('cantidad', models.DecimalField(decimal_places=3, max_digits=8)),
            ],
        ),
    ]
