from django.db import models

# Create your models here.

class  Sucursal(models.Model):
    id_sucursal = models.CharField(primary_key=True,max_length=6)
    nombre_sucursal = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    horarios = models.CharField(max_length=50)
    celular = models.CharField(max_length=100)
    encargado = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_sucursal
    