from django.db import models
from datetime import date

class Nave(models.Model):
    nombre = models.CharField(max_length=100)

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    nave = models.ForeignKey(Nave, on_delete=models.CASCADE, related_name="departamentos")

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=100, unique=True)
    contraseña = models.CharField(max_length=128)  # Se usará el sistema de autenticación de Django
    is_superuser = models.BooleanField(default=False)

class Trabajador(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name="trabajadores")
    puesto_trabajo = models.CharField(max_length=100)

class Impresora(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ip = models.GenericIPAddressField(null=True, blank=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name="impresoras")

class Equipo(models.Model):
    numero_serie = models.CharField(max_length=100, primary_key=True)
    tipo = models.CharField(max_length=50)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    fecha_entrega = models.DateField(default=date.today)
    fecha_devolucion = models.DateField(null=True, blank=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, related_name="equipos")
    impresoras = models.ManyToManyField(Impresora, blank=True, related_name="equipos")
