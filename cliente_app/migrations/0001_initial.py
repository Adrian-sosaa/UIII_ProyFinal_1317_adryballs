# Generated by Django 5.1.2 on 2024-12-04 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.IntegerField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('numero_productos_adquiridos', models.IntegerField()),
                ('tipo_de_pago', models.CharField(max_length=50)),
                ('fecha_nac', models.DateField()),
            ],
        ),
    ]