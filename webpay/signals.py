"""
Signal conecta tu sistema con la aplicacion desacoplada
"""
from django.dispatch import Signal

#Pago satisfactorio
pago_fue_satisfactorio = Signal()

#Respuesta invalida
respuesta_invalida = Signal()

#Monto invalido
monto_invalido = Signal()

#Mac invalido
mac_invalido = Signal()
