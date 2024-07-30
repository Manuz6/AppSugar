from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    
#class Empleado(models.Model):   Class Empleado se implementerá más adelante con un boton para el ingreso exclusivo de los empleados a su sección
#    nombre = models.CharField(max_length=30)
#    apellido = models.CharField(max_length=30)
#    email = models.EmailField()

#class Producto(models.Model):
#    nombre = models.CharField(max_length=50)
#    sector_uso = models.CharField(max_length=30)
#    proveedor = models.CharField(max_length=30)
    
class Pedidos(models.Model): 
    nombre = models.CharField(max_length=30)
    pedido = models.CharField(max_length=200)
    fecha_de_entrega = models.DateField()
    
class Reservas(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    horario = models.IntegerField()
    mesa = models.IntegerField()
    
    
