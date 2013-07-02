#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from webpay.models import OrdenCompraWebpay


class OderCompraWebpayAdmin(admin.ModelAdmin):
    """Modelo de administracion de Ordenes de Webpay
    """
    list_display = ("id", "orden_compra", "respuesta", "monto", "codigo_autorizacion", "tipo_pago", "fecha_transaccion", "status", "numero_cuota")
    search_fields = ["orden_compra", "fecha_transaccion"]
    list_per_page = 100
admin.site.register(OrdenCompraWebpay, OderCompraWebpayAdmin)
