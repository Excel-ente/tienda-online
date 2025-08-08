from django.db import models
from django.conf import settings
from decimal import Decimal
from productos.models import Producto

ESTADO_CHOICES = [
    ('nuevo', 'Nuevo'),
    ('pagado', 'Pagado'),
    ('en_proceso', 'En proceso'),
    ('enviado', 'Enviado'),
    ('cancelado', 'Cancelado'),
]

class Pedido(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    nombre_cliente = models.CharField(max_length=200)
    email_cliente = models.EmailField()
    telefono_cliente = models.CharField(max_length=50)
    direccion_envio = models.CharField(max_length=255)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='nuevo')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    envio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_pedido = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notas = models.TextField(blank=True)

    def recalc_totales(self):
        subtotal = sum([d.subtotal for d in self.detalles.all()])
        self.subtotal = subtotal
        self.total_pedido = subtotal - self.descuento + self.envio
        self.save(update_fields=['subtotal', 'total_pedido'])

    def __str__(self):
        return f"Pedido {self.id}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.SET_NULL)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def subtotal(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"{self.pedido.id} - {self.producto}"

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

@receiver(post_save, sender=DetallePedido)
@receiver(post_delete, sender=DetallePedido)
def actualizar_totales(sender, instance, **kwargs):
    instance.pedido.recalc_totales()
