from django.db import models

class MiTabla(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    Poblacion = models.CharField(max_length=100)
    Curso = models.DateField()
    Clase = models.CharField(max_length=100)
    Edad = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nombre

class Student(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class Teacher(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"



