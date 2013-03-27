#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import cgi
import commands
import tempfile
from datetime import datetime
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from webpay.models import OrdenCompraWebpay
from webpay.conf import *
from webpay.utils import recupera_file, borra_file


@require_POST
@csrf_exempt
def compra_webpay(request):
    """
    Vista de Cierre de la compra que manejara la respuesta de Transbank.
    Es ejecutada por el CGI tbk_bp_resultado.cgi
    Recibira por metodo POST
    Validacion de MAC.
    Validacion de monto.
    Validacion de orden de compra.
    """
    success = False
    req = request
    qs = _get_order_params(req)
    orden_compra = req.POST.get('TBK_ORDEN_COMPRA')
    respuesta = req.POST.get('TBK_RESPUESTA')
    monto = int(req.POST.get('TBK_MONTO')) / 100
    codigo_autorizacion = req.POST.get('TBK_CODIGO_AUTORIZACION')
    id_transaccion = req.POST.get('TBK_ID_TRANSACCION')
    final_num_tarjeta = req.POST.get('TBK_FINAL_NUMERO_TARJETA')
    id_sesion = req.POST.get("TBK_ID_SESION")
    #Comprueba archivo
    try:
        dat = recupera_file(orden_compra, monto).split("&&")
        dat_orden = dat[0]
        dat_monto = dat[1]
        borra_file(orden_compra, monto)
    except IOError:
        raise
    if orden_compra == dat_orden:
        orden = OrdenCompraWebpay(
            orden_compra=orden_compra,
            fecha_transaccion=datetime.today())
        if respuesta == "0":
            print monto, dat_monto
            if int(monto) == int(dat_monto):
                #Valida MAC
                if _valida_mac(qs) == VALID_MAC_RESPONSE:
                    orden.id_transaccion = id_transaccion
                    orden.codigo_transaccion = respuesta
                    orden.codigo_autorizacion = codigo_autorizacion
                    orden.final_num_tarjeta = final_num_tarjeta
                    orden.id_sesion = id_sesion
                    orden.codigo_autorizacion = codigo_autorizacion
                    orden.status = "Pagado"
                    success = True
                else:
                    orden.status = "MAC Invalido"
            else:
                orden.status = "Monto Invalido"
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
    #print commands.getoutput(command).strip()
    os.remove(temp_path)
    return VALID_MAC_RESPONSE if valid_mac else RECHAZADO_RESPONSE

def _get_order_params(req):
    """Ordenar los parametros recibidos, separados con &"""
    # varform = "TBK_ORDEN_COMPRA="+req.POST["TBK_ORDEN_COMPRA"]+"&"+"TBK_TIPO_TRANSACCION="+req.POST["TBK_TIPO_TRANSACCION"]+"&"+"TBK_RESPUESTA="+req.POST["TBK_RESPUESTA"]+"&"+"TBK_MONTO="+req.POST["TBK_MONTO"]+"&"+"TBK_CODIGO_AUTORIZACION="+req.POST["TBK_CODIGO_AUTORIZACION"]+"&"+"TBK_FINAL_NUMERO_TARJETA="+req.POST["TBK_FINAL_NUMERO_TARJETA"]+"&"+"TBK_FECHA_CONTABLE="+req.POST["TBK_FECHA_CONTABLE"]+"&"+"TBK_FECHA_TRANSACCION="+req.POST["TBK_FECHA_TRANSACCION"]+"&"+"TBK_HORA_TRANSACCION="+req.POST["TBK_HORA_TRANSACCION"]+"&"+"TBK_ID_SESION="+req.POST["TBK_ID_SESION"]+"&"+"TBK_ID_TRANSACCION="+req.POST["TBK_ID_TRANSACCION"]+"&"+"TBK_TIPO_PAGO="+req.POST["TBK_TIPO_PAGO"]+"&"+"TBK_NUMERO_CUOTAS="+req.POST["TBK_NUMERO_CUOTAS"]+"&"+"TBK_TASA_INTERES_MAX="+req.POST["TBK_TASA_INTERES_MAX"]+"&"+"TBK_VCI="+req.POST["TBK_VCI"]+"&"+"TBK_MAC="+req.POST["TBK_MAC"]
    # return varform
    return '&'.join(['%s=%s' % (k,v) for k,v in cgi.parse_qsl(req.body)])
