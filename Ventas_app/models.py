from django.db import models

# Create your models here.

class  Ventas(models.Model):
    id_venta = models.CharField(primary_key=True,max_length=6)
    nombre_venta = models.CharField(max_length=45)
    fecha = models.CharField(max_length=45)
    hora = models.CharField(max_length=10)
    id_producto = models.IntegerField(max_length=11)
    id_cliente = models.IntegerField(max_length=11)
    id_trabajador = models.IntegerField(max_length=11)
    cantidad = models.IntegerField(max_length=6)
    registro = models.CharField(max_length=45)
    lugar = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre_venta
    