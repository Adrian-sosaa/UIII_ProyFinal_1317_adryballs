# Generated by Django 5.1 on 2024-12-04 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('direccion', models.CharField(max_length=100)),
                ('destinatario', models.CharField(max_length=50)),
                ('cant_producto', models.IntegerField()),
                ('calidad', models.CharField(max_length=50)),
                ('id_sucursal', models.CharField(max_length=50)),
                ('id_prov', models.CharField(max_length=50)),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
