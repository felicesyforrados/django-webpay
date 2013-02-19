#!/usr/bin/env python
# -*- codding: utf-8 -*-
from django import forms

class WebPayForm(forms.Form):
    """
    Creando Formulario botón de pago y mandar a llamar
    tbk_bp_pago.cgi
    """
    prueba = forms.CharField()
    