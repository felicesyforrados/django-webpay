Django-webpay
=============

Aplicacion de integracion entre django y webpay

Instalación
===========

$ python setup.py install

Agregar url incluyendo webpay

url(r'^webpay/compra/$', include('webpay.urls')),

Crear Tablas
python manage.py schemamigration webpay --initial
