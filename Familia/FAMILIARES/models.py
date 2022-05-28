from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Familia(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    nacimiento = models.DateField()
    Parentesco = (
        ('Padre', 'Padre'),
        ('Esposo/a', 'Esposo/a'),
        ('Madre', 'Madre'),
        ('Hijo/a', 'Hijo/a'),
        ('Primo/a', 'Primo/a'),
        ('Tio/a', 'Tio/a'),
        ('Suegro/a', 'Suegro/a'),
    )
    parentesco = models.CharField(max_length=8, choices=Parentesco)

    E_civil = (
        ('Casado/a', 'Casado/a'),
        ('Soltero/a', 'Soltero/a'),
        ('Viudo/a', 'Viudo/a'),
        ('Divorciado/a', 'Divorciado/a'),
         )
    e_civil = models.CharField(max_length=12, choices=E_civil)

    def __str__(self):
        return f' NOMBRE : {self.nombre} EDAD : {self.edad} NACIMIENTO : {self.nacimiento} PARENTESCO : {self.parentesco} ESTADO_CIVIL : {self.e_civil}'