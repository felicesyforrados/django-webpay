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

°Descargando la carpeta

    $ python setup.py install

°O también agregando a requeriments.txt

    -e git+git://github.com/felicesyforrados/django-webpay.git#egg=django-webpay

Después ejecutar el comando

    $ pip install -r requirements.txt


Configuración
=============

1. Agregar vista que validara los parametros que nos de el CGI de Webpay

        # urls.py
        url(r'^webpay/compra/$', include('webpay.urls')),

2. Agregar las variables en settings.py

    °Tipo de transaccion que manejaras

        # settings.py
        TBK_TIPO_TRANSACCION = 'TR_NORMAL'

    °URL de la página de exito de tu comercio

        # settings.py
        TBK_URL_EXITO = 'http://tucomercio.com/paginaexito'

    °URL de la página de fracaso de tu comercio

        # settings.py
        TBK_URL_FRACASO = 'http://tucomercio/paginafracaso'

    °Ruta directa del CGI que esta en el KCC de Transbank

        # settings.py
        URL_CGI_PAGO = '/cgi-bin/tbk_bp_pago.cgi'

    °Ruta directa del archivo mac que validara la autenticidad de la respuesta

        # settings.py
        URL_CGI_VALIDA_MAC = '/cgi-bin/tbk_check_mac.cgi'

3. Agregar app a settings.py

        #settings.py
        ...
        INSTALLED_APPS = (
            ...,
            'webpay',
        )

4. Crear Tablas

    °South

        python manage.py schemamigration webpay --initial

Uso
===

La dinámica básica con Webpay es primero armar un formulario el cual contiene los parametros que se le enviaran al CGI 
y Webpay los pueda procesar, después Webpay tomara el control del navegador y pedira los datos del tarjetahabiente, 
Webpay es quien validara el número de la tarejta y el código, cuando todo este correcto mandara a llamar una
vista la cual es la que validara los datos entregados por Webpay, al estar todo correcto se guardara un registro 
en el modelo OrdenCompraWebpay y se enviara un Signal el cual se puede hacer uso para guardar los datos en otro
modelo si es que lo requiere el usuario.


