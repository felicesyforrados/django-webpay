#!/usr/bin/env python
# -*- codding: utf-8 -*-
from django.db import models
from webpay.signals import pago_fue_satisfactorio, respuesta_invalida, monto_invalido, mac_invalido
from webpay.conf import STATUS

class OrdenCompraWebpay(models.Model):
    orden_compra = models.CharField(max_length=42, unique=True)
    respuesta = models.CharField(max_length=30, blank=True)
    monto = models.PositiveIntegerField(default=0)
    codigo_autorizacion = models.CharField(max_length=8, blank=True)
    final_num_tarjeta = models.CharField(max_length=4, blank=True)
    tipo_pago = models.CharField(max_length=80, blank=True)
    fecha_transaccion = models.DateTimeField(blank=True, null=True)
    id_transaccion = models.CharField(max_length=80, blank=True)
    status = models.CharField(max_length=80, blank=True)
    codigo_transaccion = models.CharField(max_length=80, blank=True)
    id_sesion = models.CharField(max_length=80, blank=True)
    tipo_transaccion = models.CharField(max_length=30, blank=True)
    fecha_contable = models.CharField(max_length=20, blank=True)
    numero_cuota = models.CharField(max_length=10, blank=True)

    class Meta:
        verbose_name = "Orden de compra WebPay"

    def enviar_signals(self):
        """Eniar un Signal para la app a la que se conecto y pueda
        grabar en su propio Modelo"""
        #Pagado
        if self.status == STATUS["PAGADO"]:
            pago_fue_satisfactorio.send(sender=self)
        elif self.status == STATUS['RESP_INVALIDO']:
            #Respuesta invalida
            respuesta_invalida.send(sender=self)
        elif self.status == STATUS["MONTO_INVALIDO"]:
            #Monto invalido
            monto_invalido.send(sender=self)
        elif self.status == STATUS["MAC_INVALIDO"]:
            #Mac invalido
            mac_invalido.send(sender=self)

    def __unicode__(self):
        if self.tipo_pago == 'VN' or self.tipo_pago == 'VD':
            return "<Webpay Contado: {}>".format(self.orden_compra)
        else:
            return "<Webpay Cuotas: {}>".format(self.orden_compra)
