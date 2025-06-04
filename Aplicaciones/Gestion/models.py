from django.db import models

# Create your models here.

# Modelo Equipo
class Equipo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    entrenador = models.CharField(max_length=100)
    escudo = models.ImageField(upload_to='equipos/fotos/', null=True, blank=True)

    def _str_(self):
        fila = "{0}: {1} - {2} - {3}"
        return fila.format(self.id, self.nombre, self.ciudad, self.entrenador)