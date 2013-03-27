#!/usr/bin/env python
# -*- codding: utf-8 -*-
from django.db import models
from webpay.signals import *

class OrdenCompraWebpay(models.Model):
    orden_compra = models.CharField(max_length=42, unique=True)
    respuesta = models.CharField(max_length=2, blank=True)
    monto = models.PositiveIntegerField(default=0)
    codigo_autorizacion = models.CharField(max_length=6, blank=True)
    final_num_tarjeta = models.CharField(max_length=4, blank=True)
    tipo_pago = models.CharField(max_length=80, blank=True)
    fecha_transaccion = models.DateTimeField()
    id_transaccion = models.CharField(max_length=80, blank=True)
    status = models.CharField(max_length=80, blank=True)
    codigo_transaccion = models.CharField(max_length=80, blank=True)
    id_sesion = models.CharField(max_length=80, blank=True)

    class Meta:
        verbose_name = "Orden de compra WebPay"

    def enviar_signals(self):
        """Eniar un Signal para la app a la que se conecto y pueda
        grabar en su propio Modelo"""
        pago_fue_satisfactorio.send(sender = self)