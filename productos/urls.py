from django.urls import path
from .views import TiendaView

urlpatterns = [
    path('', TiendaView.as_view(), name='tienda'),
]
