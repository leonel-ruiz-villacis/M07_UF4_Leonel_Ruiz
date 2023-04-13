from django.db import models

class MiTabla(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    Poblacion = models.CharField(max_length=100)
    Curso = models.DateField()
    Clase = models.CharField(max_length=100)
    edad = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.campo1

