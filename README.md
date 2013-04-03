Django-webpay
=============

Aplicacion de integracion entre Django y Webpay. Es necesario tener en cuenta
las recomendaciones del manual para entener el procedimiento que se requiere.

Esta app ayuda a la integración con Webpay en tu app Django sin embargo se debe
contemplar lo siguiente:

1. La realización de tus páginas de exito/fracaso.
2. El alojo de la carpeta cgi-bin en tu servidor.
3. Permisos adecuados para los CGI.
4. Configuración adecuada del archivo tbk_config.dat requerido por Webpay.
5. Generación de las llaves de cifrado.


Instalación
===========

Extisten dos opciones para instalarlo, estas son:

Descargando la carpeta
----------------------

$ python setup.py install

Agregando a requeriments.txt
----------------------------
-e git+git://github.com/felicesyforrados/django-webpay.git#egg=django-webpay

pip install -r requirements.txt


Configuración
=============

1. Agregar vista que validara los parametros que nos de el CGI de Webpay

url(r'^webpay/compra/$', include('webpay.urls')),

2. Agregar las variables en settings.py

Tipo de transaccion que manejaras
---------------------------------
TBK_TIPO_TRANSACCION = 'TR_NORMAL'

URL de la página de exito de tu comercio
----------------------------------------
TBK_URL_EXITO = 'http://tucomercio.com/paginaexito'

URL de la página de fracaso de tu comercio
------------------------------------------
TBK_URL_FRACASO = 'http://tucomercio/paginafracaso'

Ruta directa del CGI que esta en el KCC de Transbank
----------------------------------------------------
URL_CGI_PAGO = '/cgi-bin/tbk_bp_pago.cgi'

Ruta directa del archivo mac que validara la autenticidad de la respuesta
-------------------------------------------------------------------------
URL_CGI_VALIDA_MAC = '/cgi-bin/tbk_check_mac.cgi'

3. Agregar app a settings.py
    ...
    INSTALLED_APPS = (
        ..
        'webpay',
    )
    ...

4. Crear Tablas

Con South
---------
python manage.py schemamigration webpay --initial

