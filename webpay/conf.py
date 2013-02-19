#-*- codding: utf-8 -*-

#Response
ACEPTADO_RESPONSE = 'ACEPTADO'
RECHAZADO_RESPONSE = 'RECHAZADO'
VALID_MAC_RESPONSE = 'CORRECTO'

#Codigos de respuesta
TRANSACTION_CODES = {
    '0':('Transacción aprobada.'),
    '-1':('Rechazo de transacción.'),
    '-2': ('Transacción debe reintentarse.'),
    '-3': ('Error en transacción.'),
    '-4': ('Rechazo de transacción.'),
    '-5': ('Rechazo por error de tasa.'),
    '-6': ('Excede cupo máximo mensual.'),
    '-7': ('Excede limite diario de transacción.'),
    '-8': ('Rubro no autorizado.')
}