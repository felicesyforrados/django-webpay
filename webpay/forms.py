#!/usr/bin/env python
# -*- codding: utf-8 -*-
from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe


class WebPayNormalForm(forms.Form):
    """
    Formulario 'Normal' manda a llamar tbk_bp_pago.cgi
    Los parametros se encuentran ocultos.
    En base a la documentación se necesitan enviar los siguientes parametros:
    TBK_TIPO_TRANSACCION
    TBK_MONTO
    TBK_ORDEN_COMPRA
    TBK_ID_SESION
    TBK_URL_EXITO
    TBK_URL_FRACASO
    """
    TBK_TIPO_TRANSACCION = forms.CharField(label='', widget = forms.TextInput(
        attrs={'readonly':'readonly',
            'style':'display:none;',
            'id': 'TBK_TIPO_TRANSACCION'}))
    TBK_MONTO = forms.CharField(label='', widget = forms.TextInput(
        attrs={'readonly':'readonly',
            'style':'display:none;',
            'id': 'TBK_MONTO'}))
    TBK_ORDEN_COMPRA = forms.CharField(label='', widget = forms.TextInput(
        attrs={'readonly':'readonly',
        'style':'display:none;',
        'id': 'TBK_ORDEN_COMPRA'}))
    TBK_ID_SESION = forms.CharField(label='', widget = forms.TextInput(
        attrs={'readonly':'readonly',
            'style':'display:none;',
            'id': 'TBK_ID_SESION'}))
    TBK_URL_EXITO = forms.CharField(label='', widget = forms.TextInput(
        attrs={'readonly':'readonly',
            'style':'display:none;',
            'id': 'TBK_URL_EXITO'}))
    TBK_URL_FRACASO = forms.CharField(label='', widget = forms.TextInput(
        attrs={'readonly':'readonly',
            'style':'display:none;',
            'id': 'TBK_URL_FRACASO'}))

    def __init__(self, *args, **kwargs):
        super(WebPayNormalForm, self).__init__(*args, **kwargs)

    def render(self):
        return mark_safe(u"""<form action="%s" method="POST">%s<input type="image" src="%s" border="0" name="submit" width='200' height='140'></form>""" % (settings.URL_CGI_PAGO, self, settings.URL_IMG_BTN_WEBPAY))