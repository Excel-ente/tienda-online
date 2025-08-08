import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from .models import Pedido, DetallePedido
from usuarios.models import Direccion
from productos.models import Producto

@login_required
@require_GET
def mis_pedidos(request):
    pedidos = Pedido.objects.filter(user=request.user).order_by('-fecha_creacion')[:20]
    data = []
    for p in pedidos:
        data.append({
            'id': p.id,
            'fecha': p.fecha_creacion.isoformat(),
            'total': float(p.total_pedido),
            'productos': [
                {
                    'nombre': d.producto.nombre if d.producto else '',
                    'cantidad': d.cantidad,
                    'precio_unitario': float(d.precio_unitario),
                    'subtotal': float(d.subtotal)
                } for d in p.detalles.all()
            ],
            'cliente': {
                'nombre': p.nombre_cliente,
                'email': p.email_cliente,
                'telefono': p.telefono_cliente,
            }
        })
    return JsonResponse({'pedidos': data})

@require_POST
def checkout(request):
    data = json.loads(request.body.decode('utf-8'))
    items = data.get('items', [])
    direccion_id = data.get('direccion_id')
    direccion = Direccion.objects.get(id=direccion_id) if direccion_id else None
    pedido = Pedido.objects.create(
        user=request.user if request.user.is_authenticated else None,
        nombre_cliente=direccion.usuario.username if direccion else data.get('nombre',''),
        email_cliente=data.get('email',''),
        telefono_cliente=data.get('telefono',''),
        direccion_envio=str(direccion) if direccion else data.get('direccion',''),
    )
    for item in items:
        producto = Producto.objects.get(id=item['product_id'])
        DetallePedido.objects.create(
            pedido=pedido,
            producto=producto,
            cantidad=item.get('cantidad',1),
            precio_unitario=producto.precio,
        )
    pedido.recalc_totales()
    return JsonResponse({'pedido_id': pedido.id})
