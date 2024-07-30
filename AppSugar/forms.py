from django import forms

class Pedidos_Formulario(forms.Form):
    nombre = forms.CharField()
    pedido = forms.CharField()
    fecha_entrega = forms.DateField()
    
    
class Clientes_Api(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class Busca_Cliente(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.CharField()