from django.db import models

# Create your models here.

class  Ingredientes(models.Model):
    id_ingrediente = models.CharField(primary_key=True,max_length=6)
    nombre_ingrediente = models.CharField(max_length=45)
    caducidad = models.CharField(max_length=45)
    codigo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=100)
    cantidad = models.IntegerField(max_length=10)
    id_sucursal = models.IntegerField(max_length=11)

    def __str__(self):
        return self.nombre_ingrediente
    