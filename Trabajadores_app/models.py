from django.db import models

# Create your models here.

class  Trabajadores(models.Model):
    id_trabajador = models.CharField(primary_key=True,max_length=6)
    nombre_trabajador = models.CharField(max_length=45)
    apellido_P = models.CharField(max_length=45)
    apellido_M = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    fecha_de_nacimiento = models.CharField(max_length=20)
    celular = models.CharField(max_length=10)
    genero = models.CharField(max_length=9)

    def __str__(self):
        return self.nombre_trabajador
    