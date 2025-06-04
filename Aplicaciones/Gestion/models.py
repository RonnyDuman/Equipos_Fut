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
    

# Modelo Jugador
class Jugador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=100)
    numero_camiseta = models.IntegerField()
    foto = models.ImageField(upload_to='jugadores/fotos/', null=True, blank=True)
    ficha_pdf = models.FileField(upload_to='jugadores/pdfs/', null=True, blank=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

    def _str_(self):
        fila = "{0}: {1} - {2} - {3} - {4}"
        return fila.format(self.id, self.nombre, self.posicion, self.numero_camiseta, self.equipo)