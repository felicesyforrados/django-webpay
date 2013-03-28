#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from django.test import TestCase
from django.test.client import Client
from webpay.models import OrdenCompraWebpay
from webpay.conf import RECHAZADO_RESPONSE
from webpay.signals import *

WEBPAY_PARAMS = {
    "TBK_ORDEN_COMPRA": "fyf_1364257085_79764",
    "TBK_TIPO_TRANSACCION": "TR_NORMAL",
    "TBK_RESPUESTA": "0",
    "TBK_MONTO": "12000",
    "TBK_CODIGO_AUTORIZACION": "692157",
    "TBK_FINAL_NUMERO_TARJETA": "6623",
    "TBK_FECHA_CONTABLE": "0325",
    "TBK_FECHA_TRANSACCION": "0325",
    "TBK_HORA_TRANSACCION": "214711",
    "TBK_ID_SESION": "fyf_79764",
    "TBK_ID_TRANSACCION": "4257087822",
    "TBK_TIPO_PAGO": "VD",
    "TBK_NUMERO_CUOTAS": "0",
    "TBK_TASA_INTERES_MAX": "0",
    "TBK_VCI":"TSY",
    "TBK_MAC":"0a527253af47f13cd4299b1fc95301009c2d2c56fe448471fbb4437a436aa1ec87eea85b8974ed3ecb416b388ac68f1ad36bb3f3ca96ea2cb19cb310ec9597ac0eb8b75114ca4ac8adfc894cc1caa3792bad86038a21fcfd7ef68853a3c2cfd3c7fca3429030f63e38f6995f6db9e71da7a51fb754975aef14f663a60d9437820acab20d9585e99640a5dc4645c5f1d70f69b07f9cd16b18ed26d3641cb07be8c6c415368769b91ebdf0e9c431f6b2921a5d5b5bcafb0976b7c90c6c6209a9245d0b06ab397dbd41dd469f9fadf2389d29d6254c756083c7f4184754a2adf21e24b774dab81dd2b97e5ea8640d590eb91c85abfd320ebfaaa730b1943991ff4a6d145a191c70d66d5dd11f1aac571b8ea3d098a2e682fd931ab5236b08a8741aee2ca2b77dd629e80e54fd4c3b38ee758b9cbe67fe8fd1770bd3c44e06166fb9817497adfecdc99bcc8f2d76306b69678d069e871a5601f72818c7961d26a5d9d7088e215f13bfb6ce87759abadfa99069beb574aa80f6805464345eab8f326fa749b6b11bbabf30fc9d822ff815360d27f9c60276e4b113f56bfd9a64261096fd130ce4101a52ffd2af6e253b4f54b2f86bb0e04861fea731dbaf08305bde3f5f53d1e8aa8de37fecc427a8948ea5c518b312f16ae9bd6d6aadb7e84f4c812c88be0bbe2886e016dce02aa00ed3db39125d2955b04a55bd957ca62c1bbc62bd"
}


class WebpayTest(TestCase):
    def setUp(self):
        self.params = WEBPAY_PARAMS.copy()

    def test_no_registro(self):
        #Archivo no existe
        params = self.params
        with self.assertRaises(OrdenCompraWebpay.DoesNotExist):
            response = self.client.post("/", params)

    def test_respuesta(self):
        #Crear Archivo Respuesta != 0
        params = self.params
        params["TBK_RESPUESTA"] = "8"
        ord_m = OrdenCompraWebpay(
            orden_compra=params["TBK_ORDEN_COMPRA"],
            monto=int(params["TBK_MONTO"])/100)
        ord_m.save()
        response = self.client.post("/", params)
        for i in response:
            self.assertEqual(i, RECHAZADO_RESPONSE)
        orden = OrdenCompraWebpay.objects.all()
        self.assertEqual(orden[0].status, "Invalido")

    def test_monto(self):
        #Validar monto diferente
        params = self.params
        params["TBK_MONTO"] = "800"
        ord_m = OrdenCompraWebpay(
            orden_compra=params["TBK_ORDEN_COMPRA"],
            monto=int(WEBPAY_PARAMS["TBK_MONTO"])/100)
        ord_m.save()
        response = self.client.post("/", params)
        for i in response:
            self.assertEqual(i, RECHAZADO_RESPONSE)
        orden = OrdenCompraWebpay.objects.all()
        self.assertEqual(orden[0].status, "Monto Invalido")

    def test_mac(self):
        #Validar MAC invalido
        params = self.params
        params["TBK_MAC"] = "8321321321"
        ord_m = OrdenCompraWebpay(
            orden_compra=params["TBK_ORDEN_COMPRA"],
            monto=int(params["TBK_MONTO"])/100)
        ord_m.save()
        response = self.client.post("/", params)
        for i in response:
            self.assertEqual(i, RECHAZADO_RESPONSE)
        orden = OrdenCompraWebpay.objects.all()
        self.assertEqual(orden[0].status, "MAC Invalido")

    def test_ok(self):
        params = self.params
        ord_m = OrdenCompraWebpay(
            orden_compra=params["TBK_ORDEN_COMPRA"],
            monto=int(params["TBK_MONTO"])/100)
        ord_m.save()
        response = self.client.post("/", params)
