from django.db import models

# Create your models here.
class Pedido(models.Model): 
    producto = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    precio = models.FloatField()
    ubicacion = models.CharField(max_length=100)