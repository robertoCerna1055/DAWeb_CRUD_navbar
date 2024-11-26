from django.db import models

# Create your models here.

class  Platillo(models.Model):
    id_platillo = models.CharField(primary_key=True,max_length=6)
    nombre_platillo = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=100)
    ingredientes = models.CharField(max_length=100)
    precio = models.IntegerField(max_length=10)
    calorias = models.IntegerField(max_length=10)
    tipo = models.CharField(max_length=45)
    cantidad = models.IntegerField(max_length=10)

    def __str__(self):
        return self.nombre_platillo
    