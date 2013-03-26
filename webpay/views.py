#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import cgi
import commands
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from webpay.models import OrdenCompraWebpay
from webpay.conf import *

@require_POST
@csrf_exempt
def compra_webpay(request):
    """
    Vista de Cierre de la compra que manejara la respuesta de Transbank. Es ejecutada por el CGI tbk_bp_resultado.cgi
    Recibira por metodo POST
    Validacion de MAC.
    Validacion de monto.
    Validacion de orden de compra.
    """
    success = False
    orden_compra = request.POST.get('TBK_ORDEN_COMPRA')
    respuesta = request.POST.get('TBK_RESPUESTA')
    monto = request.POST.get('TBK_MONTO')
    codigo_autorizacion = request.POST.get('TBK_CODIGO_AUTORIZACION')
    id_transaccion = request.POST.get('TBK_ID_TRANSACCION')
    final_num_tarjeta = request.POST.get('TBK_FINAL_NUMERO_TARJETA')
    qs = _get_qs(request)
    orden = OrdenCompraWebpay.objects.get(unique_id=orden_compra)
    orden.id_transaccion = id_transaccion
    orden.codigo_transaccion = respuesta
    orden.codigo_autorizacion = codigo_autorizacion
    orden.final_num_tarjeta = final_num_tarjeta
    orden.
    if respuesta == "0" and monto == '12':
        #Valida MAC
        if _valida_mac(qs) == VALID_MAC_RESPONSE:
            if orden.monto == monto and not orden.codigo_autorizacion:
                orden.codigo_autorizacion = codigo_autorizacion
                orden.status = "Pagado"
                success = True
            else:
                orden.status = "Monto invalido"
        else:
            orden.status = "MAC Invalido"
    else:
        orden.status = "Invalido"
    orden.save()
    orden.enviar_signals()
    return HttpResponse(ACEPTADO_RESPONSE) if success else HttpResponse(RECHAZADO_RESPONSE)

def _valida_mac(qs):
    """Funcion que validara la MAC que viene de resultado.cgi. Se debe generar
    un archivo de texto con los parametros recibidos en el formato en el que
    llegan, entregar la ubicacion del archivo
    """
    descriptor, temp_path = tempfile.mkstemp()
    f = os.fdopen(descriptor, "w")
    f.write(qs)
    f.close()
    command = "%(mac)s %(temp_path)s" % {
        "mac" : settings.URL_CGI_VALIDA_MAC,
        "temp_path": temp_path
    }
    valid_mac = commands.getoutput(command).strip() == VALID_MAC_RESPONSE
    os.remove(temp_path)
    return VALID_MAC_RESPONSE if valid_mac else RECHAZADO_RESPONSE

def _get_order_params(request):
    """Ordenar los parametros recibidos, separados con &"""
    return "&".join(["%s=%s" % (i, j) for i, j in cgi.parse_qsl(request.body)])