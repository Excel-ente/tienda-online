from django.views.generic import TemplateView
from django.http import JsonResponse
from .models import Producto, Categoria
from conf.models import Empresa

class TiendaView(TemplateView):
    template_name = 'tienda.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        empresa = Empresa.objects.first()
        tiendas = empresa.tiendas.all() if empresa else []
        tienda_id = self.request.GET.get('tienda')
        tienda_actual = None
        if tiendas:
            if tienda_id:
                tienda_actual = tiendas.filter(id=tienda_id).first()
            else:
                tienda_actual = tiendas.first()
        productos = Producto.objects.filter(publicado=True)
        productos_json = [
            {
                'id': p.id,
                'name': p.nombre,
                'price': float(p.precio),
                'image': p.imagen.url if p.imagen else '',
                'barcode': p.barcode,
                'description': p.descripcion,
                'unitsPerBox': p.unitsPerBox,
                'stock': {'units': p.stock_units},
                'category': p.categoria_id,
            }
            for p in productos
        ]
        context.update({
            'empresa': empresa,
            'tiendas': tiendas,
            'tienda_actual': tienda_actual,
            'productos_json': productos_json,
            'categorias': Categoria.objects.all(),
        })
        return context
