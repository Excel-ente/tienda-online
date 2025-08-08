from django.db import models
from django.conf import settings

class Direccion(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='direcciones')
    calle = models.CharField(max_length=200)
    numero = models.CharField(max_length=50)
    piso = models.CharField(max_length=50, blank=True)
    localidad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    cp = models.CharField(max_length=20)
    pais = models.CharField(max_length=100)
    observaciones = models.TextField(blank=True)
    predeterminada = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.calle} {self.numero}"

class PerfilUsuario(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username
