from django.db import models

class Cupon(models.Model):
    TIPO_CHOICES = [
        ('porcentaje', 'Porcentaje'),
        ('monto', 'Monto'),
    ]
    codigo = models.CharField(max_length=50, unique=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)
    vigencia_desde = models.DateField(null=True, blank=True)
    vigencia_hasta = models.DateField(null=True, blank=True)
    uso_maximo = models.IntegerField(default=0)
    uso_actual = models.IntegerField(default=0)

    def __str__(self):
        return self.codigo

class Promocion(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)
    banner = models.ImageField(upload_to='promos', blank=True, null=True)
    url_destino = models.URLField(blank=True)
    prioridad = models.IntegerField(default=0)
    segmento = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.titulo
