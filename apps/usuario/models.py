from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
	nombre = models.CharField(max_length=50)
	apellidoP = models.CharField(max_length=20)
	apellidoM = models.CharField(max_length=20)
	correo = models.EmailField()
	password = models.CharField(max_length=15, null=True)
	sexo = models.CharField(max_length=10)
	edad = models.IntegerField()
	nacimiento = models.DateField()
	telefono = models.IntegerField()
	domicilio = models.TextField()
