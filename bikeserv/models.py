from django.db import models

# Create your models here.

class Persona (models.Model):
    rut = models.CharField(max_length=10)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    comuna_opc = (
        ('La Reina','La Reina'),
        ('Providencia','Providencia'),
        ('Ñuñoa','Ñuñoa'),
    )
    comuna = models.CharField(max_length=20, choices=comuna_opc)
    cred = models.IntegerField()
    def __str__(self):
        return self.nombres

class Bicicleta (models.Model):
    cod = models.IntegerField()
    def __str__(self):
        return self.cod