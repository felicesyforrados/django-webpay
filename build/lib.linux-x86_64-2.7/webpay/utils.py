#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf import settings
import os


def crea_tmp_file(orden_compra, monto):
    """Crea el archivo temporal que ayudara a comprobar los datos en 
    la pagina de cierre"""
    ruta = '%s/data_%s.log' % (settings.FOLDER_DATA_LOG, orden_compra)
    monto = int(monto) / 100
    try:
        f = open(ruta, 'w')
        f.write("%s&&%s" % (orden_compra, monto))
        f.closed
        return True
    except IOError:
        print os.getcwd(), ruta
        raise
        return os.getcwd()

def recupera_file(orden_compra, monto):
    """Recupera el archivo temporal para verificar en la pagina de cierre"""
    ruta = '%s/data_%s.log' % (settings.FOLDER_DATA_LOG, orden_compra)
    f = open(ruta, 'r')
    return f.read()

def borra_file(orden_compra, monto):
    ruta = '%s/data_%s.log' % (settings.FOLDER_DATA_LOG, orden_compra)
    os.remove(ruta)
