#!/usr/bin/env python
# -*- codding: utf-8 -*-
from django.db import models


class OrdenCompraWebpay(models.Model):
    orden_compra = models.AutoField('id', primary_key=True)
    respuesta = models.CharField(max_length=2, blank=True)
    monto = models.PositiveIntegerField(default=0)
    codigo_autorizacion = models.CharField(max_length=6, blank=True)
    final_num_tarjeta = models.CharField(max_length=4, blank=True)
    tipo_pago = models.CharField(max_length=80, blank=True)
    fecha_transaccion = models.DateTimeField()
    id_transaccion = models.CharField(max_length=80, blank=True)

    class Meta:
        verbose_name = "Orden de compra WebPay"