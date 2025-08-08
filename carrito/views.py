from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from productos.models import Producto

CART_SESSION_ID = 'cart'

def _get_cart(request):
    return request.session.setdefault(CART_SESSION_ID, {})

@require_POST
def add(request):
    cart = _get_cart(request)
    product_id = request.POST.get('product_id')
    qty = int(request.POST.get('cantidad', 1))
    producto = Producto.objects.get(id=product_id)
    item = cart.get(product_id, {'nombre': producto.nombre, 'precio': float(producto.precio), 'cantidad': 0, 'imagen': producto.imagen.url if producto.imagen else '',})
    nueva_cant = item['cantidad'] + qty
    if nueva_cant > producto.stock_units:
        return JsonResponse({'error': 'stock_insuficiente'}, status=400)
    item['cantidad'] = nueva_cant
    cart[product_id] = item
    request.session.modified = True
    return JsonResponse({'ok': True, 'cart': cart})

@require_POST
def set_quantity(request):
    cart = _get_cart(request)
    product_id = request.POST.get('product_id')
    qty = int(request.POST.get('cantidad', 1))
    if product_id in cart:
        producto = Producto.objects.get(id=product_id)
        if qty > producto.stock_units:
            return JsonResponse({'error': 'stock_insuficiente'}, status=400)
        cart[product_id]['cantidad'] = qty
        request.session.modified = True
    return JsonResponse({'ok': True, 'cart': cart})

@require_POST
def remove(request):
    cart = _get_cart(request)
    product_id = request.POST.get('product_id')
    cart.pop(product_id, None)
    request.session.modified = True
    return JsonResponse({'ok': True, 'cart': cart})

@require_GET
def summary(request):
    cart = _get_cart(request)
    return JsonResponse({'items': cart})
