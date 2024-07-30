from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *



def inicio(request):
    return render(request, "AppSugar/index.html")

def nosotros(request):
    return render(request, "AppSugar/Nosotros.html")

def producto(request):
    return render(request, "AppSugar/Producto.html")

def reservas(request):
    return render(request, "AppSugar/Reservas.html")

def tienda(request):
    return render(request, "AppSugar/Tienda.html")

def formulario_reserva(request):
    
    if request.method == 'POST':
    
        reserva = Reservas(nombre = request.POST['nombre'], apellido = request.POST['apellido'], horario = request.POST['horario'], mesa = request.POST['mesa'])
        reserva.save()
        
        return render(request, "AppSugar/index.html")
    return render (request, "AppSugar/formulario_reservas.html")

def Pedidos_formularioApi(request):

    if request.method == "POST":
        mi_pedido = Pedidos_Formulario(request.POST) 
        if mi_pedido.is_valid():
            Pedido = mi_pedido.cleaned_data
            
            Encargo = Pedidos(nombre=Pedido["nombre"], Pedido=Pedido["Pedido"], fecha_de_entrega=Pedido["Fecha_Entrega"])
            Encargo.save()

            return render(request, "AppSugar/index.html")
    else:
        mi_pedido = Pedidos_Formulario()

    return render(request, "AppSugar/pedidos_api.html", {"mi_pedido": mi_pedido})

def Registro_clientes_api(request):
    if request.method == "POST":
        Nuevo_Cliente = Clientes_Api(request.POST)
        if Nuevo_Cliente.is_valid():
            Registro = Nuevo_Cliente.cleaned_data
            
            Clientes = Cliente(nombre=Registro["nombre"], apellido=Registro["apellido"], email=Registro["email"])
            Clientes.save()

            return render(request, "AppSugar/index.html")
    else:
        Nuevo_Cliente = Clientes_Api()

    return render(request, "AppSugar/clientes_api.html", {"Nuevo_Cliente": Nuevo_Cliente})

def buscar_clientes_api(request):
    if request.method == "POST":
        mi_cliente = Busca_Cliente(request.POST)

        if mi_cliente.is_valid():
            Cliente_Busc_Api = mi_cliente.cleaned_data
            
            Cliente_Busqueda = Cliente.objects.filter(nombre__icontains=Cliente_Busc_Api["nombre"], apellido__icontains=Cliente_Busc_Api["apellido"], email__icontains=Cliente_Busc_Api["email"])

            return render(request, "AppSugar/mostrar_clientes.html", {"Cliente_Busqueda": Cliente_Busqueda})
    else:
        mi_cliente = Busca_Cliente()

    return render(request, "AppCoder/buscar_cliente_con_api.html", {"mi_cliente": mi_cliente})

