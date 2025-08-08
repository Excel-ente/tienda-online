from django.urls import path
from . import views

urlpatterns = [
    path('api/mis-pedidos/', views.mis_pedidos, name='mis_pedidos'),
    path('api/checkout/', views.checkout, name='checkout'),
]
