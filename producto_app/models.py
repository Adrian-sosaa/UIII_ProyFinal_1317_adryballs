from django.db import models

class Producto(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    direccion = models.CharField(max_length=100, null=False)
    destinatario = models.CharField(max_length=50, null=False)
    cant_producto = models.IntegerField(null=False)
    calidad = models.CharField(max_length=50, null=False)
    id_sucursal = models.CharField(max_length=50, null=False)
    id_prov = models.CharField(max_length=50, null=False)
    stock = models.IntegerField(null=False)
