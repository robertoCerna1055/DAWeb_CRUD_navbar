from django.db import models

# Create your models here.

class  Proveedores(models.Model):
    id_proveedor = models.CharField(primary_key=True,max_length=6)
    nombre_empresa = models.CharField(max_length=45)
    horarios = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    celular = models.CharField(max_length=15)
    tipo = models.CharField(max_length=45)
    direccion = models.CharField(max_length=100)
    codigo_postal = models.IntegerField(max_length=10)

    def __str__(self):
        return self.nombre_empresa
    