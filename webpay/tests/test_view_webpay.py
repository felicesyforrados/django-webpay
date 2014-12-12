#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime

from django.test import TestCase
from django.test.client import Client
from webpay.models import OrdenCompraWebpay
from webpay.conf import RECHAZADO_RESPONSE, VALID_MAC_RESPONSE, ACEPTADO_RESPONSE
from webpay.signals import *
from webpay.views import valida_mac


class WebpayTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.WEBPAY_PARAMS = "TBK_ORDEN_COMPRA=fyf_1365025480_1mh1&TBK_TIPO_TRANSACCION=TR_NORMAL&TBK_RESPUESTA=0&TBK_MONTO=1200000&TBK_CODIGO_AUTORIZACION=101996&TBK_FINAL_NUMERO_TARJETA=6623&TBK_FECHA_CONTABLE=0403&TBK_FECHA_TRANSACCION=0403&TBK_HORA_TRANSACCION=191700&TBK_ID_SESION=fyf_1mh1&TBK_ID_TRANSACCION=5025486392&TBK_TIPO_PAGO=VN&TBK_NUMERO_CUOTAS=0&TBK_VCI=TSY&TBK_MAC=1d776ae6a14ba0033d77b544860f58917b3360505831405e43947d27abbb75112885532533ada64b06279829fbf935463604c1838b647b9662c888a1154246f9e3bd8230a4d030d9ea6de45de9ba9e3084dde115f0c785b76ad0459ce66771fbbdbe9d1e4cca7d8b955ad84b100155d593d9d24098617ab7bb18e7d54bfa7a106a8f2297f6b1cd0b345ec04a0d72311ababbf717c80f4e6446ff5a96a3ee4d87e947fec59557f68dadcb79b7fd4e0ee9f343bb837720ba8354ff2dd0ed0fffe7b0db19a0a1d73c1ca9cf1e52d5ec02d3d005796eee56cd808d217b566d09967c0a62ae4f5a9c7034dd6c520a6db488d7cda7dc3c47b2822ed4f685b248c75e1b9bf1f97ac6a9917f60e29a8e4bd5c48705e934851af5e95bda3ce0afae926e233cc5bc07172f6cfba18f2e7ae721250a2637185617e3f893891326bed704afe010f5b0f9cb92a1238adaa2f78fa53f00ad80d96fba62b63d2c65cc5b73b0c91c35193fb961ee18de4098031bb27bdb2ffb503e7ca65ede02fda0eff0a412c673edcb107d1344309e3e7bcb415e59dc1f51779a06012e5f65bf8e8a3e2556bd3275e5b4286a634c5e5c1622fa546d69e3788824344c608be879323dd93df1d9a32d25eb488897ffd26464eb82de91860f8341e6638405e0cb06dd4f955263d3b1ead3a3d1e00d77105aa10c6ae08fce6b206f74ff08845c502cb58439fa6c2810"

    def test_no_registro(self):
        #Archivo no existe
        response = self.client.post("/", self.WEBPAY_PARAMS, content_type="text/html")
        self.assertEqual(response.content, RECHAZADO_RESPONSE)

    def test_respuesta(self):
        #Crear Archivo Respuesta != 0
        params = "TBK_ORDEN_COMPRA=fyf_1365025480_1mh1&TBK_TIPO_TRANSACCION=TR_NORMAL&TBK_RESPUESTA=-1&TBK_MONTO=120&TBK_CODIGO_AUTORIZACION=101996&TBK_FINAL_NUMERO_TARJETA=6623&TBK_FECHA_CONTABLE=0403&TBK_FECHA_TRANSACCION=0403&TBK_HORA_TRANSACCION=191700&TBK_ID_SESION=fyf_1mh1&TBK_ID_TRANSACCION=5025486392&TBK_TIPO_PAGO=VN&TBK_NUMERO_CUOTAS=0&TBK_VCI=TSY&TBK_MAC=1d776"
        ord_m = OrdenCompraWebpay(
            orden_compra="fyf_1365025480_1mh1",
            monto='12000')
        ord_m.save()
        response = self.client.post("/", params, content_type="text/html")
        for i in response:
            self.assertEqual(i, ACEPTADO_RESPONSE)
        orden = OrdenCompraWebpay.objects.all()
        self.assertEqual(orden[0].status, u"Inválido")

    def test_monto(self):
        #Validar monto diferente
        params = "TBK_ORDEN_COMPRA=fyf_1365025480_1mh1&TBK_TIPO_TRANSACCION=TR_NORMAL&TBK_RESPUESTA=0&TBK_MONTO=120&TBK_CODIGO_AUTORIZACION=101996&TBK_FINAL_NUMERO_TARJETA=6623&TBK_FECHA_CONTABLE=0403&TBK_FECHA_TRANSACCION=0403&TBK_HORA_TRANSACCION=191700&TBK_ID_SESION=fyf_1mh1&TBK_ID_TRANSACCION=5025486392&TBK_TIPO_PAGO=VN&TBK_NUMERO_CUOTAS=0&TBK_VCI=TSY&TBK_MAC=1d776"
        ord_m = OrdenCompraWebpay(
            orden_compra="fyf_1365025480_1mh1",
            monto='12000')
        ord_m.save()
        response = self.client.post("/", params, content_type="text/html")
        for i in response:
            self.assertEqual(i, RECHAZADO_RESPONSE)
        orden = OrdenCompraWebpay.objects.all()
        self.assertEqual(orden[0].status, u"Monto Inválido")
        #Monto como string
        params = "TBK_ORDEN_COMPRA=fyf_1365025481_1mh1&TBK_TIPO_TRANSACCION=TR_NORMAL&TBK_RESPUESTA=0&TBK_MONTO=1d20&TBK_CODIGO_AUTORIZACION=101996&TBK_FINAL_NUMERO_TARJETA=6623&TBK_FECHA_CONTABLE=0403&TBK_FECHA_TRANSACCION=0403&TBK_HORA_TRANSACCION=191700&TBK_ID_SESION=fyf_1mh1&TBK_ID_TRANSACCION=5025486392&TBK_TIPO_PAGO=VN&TBK_NUMERO_CUOTAS=0&TBK_VCI=TSY&TBK_MAC=1d776"
        ord_m = OrdenCompraWebpay(
            orden_compra="fyf_1365025481_1mh1",
            monto='12000')
        ord_m.save()
        response = self.client.post("/", params, content_type="text/html")
        for i in response:
            self.assertEqual(i, RECHAZADO_RESPONSE)
        orden = OrdenCompraWebpay.objects.all()
        self.assertEqual(orden[0].status, u"Monto Inválido")

    def test_function_mac(self):
        #Validar funcion MAC
        self.assertEqual(valida_mac(self.WEBPAY_PARAMS), VALID_MAC_RESPONSE)

    def test_mac(self):
        #Validar MAC invalido
        params = "TBK_ORDEN_COMPRA=fyf_1365025480_1mh1&TBK_TIPO_TRANSACCION=TR_NORMAL&TBK_RESPUESTA=0&TBK_MONTO=1200000&TBK_CODIGO_AUTORIZACION=101996&TBK_FINAL_NUMERO_TARJETA=6623&TBK_FECHA_CONTABLE=0403&TBK_FECHA_TRANSACCION=0403&TBK_HORA_TRANSACCION=191700&TBK_ID_SESION=fyf_1mh1&TBK_ID_TRANSACCION=5025486392&TBK_TIPO_PAGO=VN&TBK_NUMERO_CUOTAS=0&TBK_VCI=TSY&TBK_MAC=1d776"
        ord_m = OrdenCompraWebpay(
            orden_compra="fyf_1365025480_1mh1",
            monto='12000')
        ord_m.save()
        response = self.client.post("/", params, content_type="text/html")
        for i in response:
            self.assertEqual(i, RECHAZADO_RESPONSE)
        orden = OrdenCompraWebpay.objects.all()
        self.assertEqual(orden[0].status, u"MAC Inválido")

    def test_orden_no_existe(self):
        """Test que se ejecuta cuando la orden de compra no existe o ya fue
        procesada"""
        params = "TBK_ORDEN_COMPRA=fyf_1365025480_1mh2&TBK_TIPO_TRANSACCION=TR_NORMAL&TBK_RESPUESTA=0&TBK_MONTO=120&TBK_CODIGO_AUTORIZACION=101996&TBK_FINAL_NUMERO_TARJETA=6623&TBK_FECHA_CONTABLE=0403&TBK_FECHA_TRANSACCION=0403&TBK_HORA_TRANSACCION=191700&TBK_ID_SESION=fyf_1mh1&TBK_ID_TRANSACCION=5025486392&TBK_TIPO_PAGO=VN&TBK_NUMERO_CUOTAS=0&TBK_VCI=TSY&TBK_MAC=1d776"
        ord_m = OrdenCompraWebpay(
            orden_compra="fyf_1365025480_1mh2",
            monto='12000',
            fecha_transaccion=datetime.datetime.today())
        ord_m.save()
        response = self.client.post("/", params, content_type="text/html")
        for i in response:
            self.assertEqual(i, RECHAZADO_RESPONSE)

    def test_ok(self):
        ord_m = OrdenCompraWebpay(
            orden_compra="fyf_1365025480_1mh1",
            monto='12000')
        ord_m.save()
        response = self.client.post("/", self.WEBPAY_PARAMS, content_type="text/html")
        for i in response:
            self.assertEqual(i, ACEPTADO_RESPONSE)
