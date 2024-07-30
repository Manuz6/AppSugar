from django.urls import path
from AppSugar.views import *

urlpatterns = [
    path('inicio/', inicio, name="inicio"),
    path('nosotros/', nosotros, name="nosotros"),
    path('productos/', producto, name="producto"),
    path('reservas/', reservas, name="reservas"),
    path('tienda/', tienda, name="tienda"),
    path('formulario_reserva/', formulario_reserva, name="form_reserva"),
    path('pedidos_api/', Pedidos_formularioApi, name="pedidos_api"),
    path('clientes_api/', Registro_clientes_api, name="clientes_api"),
    path('buscar_clientes/', buscar_clientes_api, name="Buscar_clientes_Api"),
    
]
