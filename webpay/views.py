#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from webpay.models import OrdenCompraWebpay
from webpay.conf import *


@csrf_exempt
def compra_webpay(request):
    """
    Vista de Cierre de la compra que manejara la respuesta de Transbank. Es ejecutada por el CGI tbk_bp_resultado.cgi
    Recibira por metodo POST
    Validacion de MAC.
    Validacion de monto.
    Validacion de orden de compra.
    """
    output = {}
    if request.method == 'POST':
        orden_compra = request.POST.get('TBK_ORDEN_COMPRA')
        respuesta = request.POST.get('TBK_RESPUESTA')
        monto = request.POST.get('TBK_MONTO')
        codigo_autorizacion = request.POST.get('TBK_CODIGO_AUTORIZACION')
        id_transaccion = request.POST.get('TBK_ID_TRANSACCION')
        final_num_tarjeta = request.POST.get('TBK_FINAL_NUMERO_TARJETA')
        #Valida Monto
        if respuesta == "0":
            if monto == '12000':
                #Valida MAC
                    #Valida Orden de Compra en la BD
                duplicado = OrdenCompraWebpay.objects.filter(orden_compra = orden_compra)
                if not duplicado:
                    output['feedback'] = ACEPTADO_RESPONSE
        else:
            #Acepta 'no autorizacion' de la transaccion
            output['feedback'] = ACEPTADO_RESPONSE
        return render(request, 'pagos/webpay_cierre.html', output)
    else:
        HttpResponse(status=400)

def _valida_mac(mac):
    """Funcion que validara la MAC que viene de resultado.cgi
    """
    pass
