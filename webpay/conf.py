#-*- codding: utf-8 -*-

#Response
ACEPTADO_RESPONSE = 'ACEPTADO'
RECHAZADO_RESPONSE = 'RECHAZADO'
VALID_MAC_RESPONSE = 'CORRECTO'

#Codigos de respuesta
TRANSACTION_CODES = {
    '0':('Transaccion aprobada.'),
    '-1':('Rechazo de transaccion.'),
    '-2': ('Transaccion debe reintentarse.'),
    '-3': ('Error en transaccion.'),
    '-4': ('Rechazo de transaccion.'),
    '-5': ('Rechazo por error de tasa.'),
    '-6': ('Excede cupo maximo mensual.'),
    '-7': ('Excede limite diario de transaccion.'),
    '-8': ('Rubro no autorizado.')}

#Estatus
STATUS = {
    "PAGADO": "Pagado",
    "MONTO_INVALIDO": "Monto Invalido",
    "MAC_INVALIDO": "MAC Invalido",
    "RESP_INVALIDO": "Invalido"
}