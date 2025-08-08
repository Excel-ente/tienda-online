from django.test import TestCase
from productos.models import Categoria, Producto
from pedidos.models import Pedido, DetallePedido

class PedidoModelTest(TestCase):
    def test_subtotal(self):
        categoria = Categoria.objects.create(nombre='Cat', slug='cat')
        producto = Producto.objects.create(nombre='Prod', categoria=categoria, descripcion='', publicado=True, precio=10, imagen='x', barcode='b', unitsPerBox=1, stock_units=5)
        pedido = Pedido.objects.create(nombre_cliente='a', email_cliente='b@c.com', telefono_cliente='123', direccion_envio='dir')
        detalle = DetallePedido.objects.create(pedido=pedido, producto=producto, cantidad=2, precio_unitario=producto.precio)
        self.assertEqual(detalle.subtotal, 20)
