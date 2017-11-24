# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Distrito(models.Model):
    """
    Se decide utilizar este modelo para la clase distrito porque es
    necesario el nombre y la cantidad de votantes,
    y en un futuro se mostrara un mapa con un marker por cada distrito
    que contenga los resultados del mismo.
    """
    nombre = models.CharField('Nombre del distrito', max_length=128)
    cantidad_votantes = models.IntegerField('Cantidad de votantes', default=0)
    latitude = models.DecimalField('Latitud', max_digits=14, decimal_places=10, default=0)
    longitude = models.DecimalField('Latitud', max_digits=14, decimal_places=10, default=0)


    def __str__(self):
        return 'Distrito {}'.format(self.nombre)

class Candidato(models.Model):
    """
    #TODO Completar segun consideraciones del desarrollador
    En este comentario escribir por que se decide modelar de esta
    forma la clase
    
    use este modelo porque se nesecita saber cuantos votos totales tiene el candidato
    """
    nombre=models.CharField(max_length=50)
    cantidad_de_votos=models.IntegerField()
    


class Votos(models.Model):
    """
    #TODO Completar segun consideraciones del desarrollador
    En este comentario escribir por que se decide modelar de esta
    forma la clase
    
    
    use este modela porque se necesita saber cuantos votos por distrito hay y por candidato en el caso que candidato sea null el voto es en blanco
    """
    candidato=models.ForeignKey(Candidato)
    cantidad_votos=models.IntegerField()
    distrito=models.ForeignKey(Distrito)
    
