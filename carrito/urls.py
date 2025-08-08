from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add, name='cart_add'),
    path('set', views.set_quantity, name='cart_set'),
    path('remove', views.remove, name='cart_remove'),
    path('summary', views.summary, name='cart_summary'),
]
