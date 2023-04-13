from django.db import models

class MiTabla(models.Model):
    campo1 = models.CharField(max_length=100)
    campo2 = models.TextField()
    campo3 = models.IntegerField()
    campo4 = models.DateField()
    campo5 = models.BooleanField()
    campo6 = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.campo1

