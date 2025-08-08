from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='categorias', blank=True, null=True)
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['orden', 'nombre']

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.SET_NULL, related_name='productos')
    descripcion = models.TextField(blank=True)
    publicado = models.BooleanField(default=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos')
    barcode = models.CharField(max_length=100)
    unitsPerBox = models.IntegerField(default=1)
    stock_units = models.IntegerField(default=0)

    class Meta:
        ordering = ['categoria', 'nombre']

    def __str__(self):
        return self.nombre
