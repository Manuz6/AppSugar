from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Pedidos)
admin.site.register(Reservas)


# SuperUser : User : Encargado , Pass : 123
