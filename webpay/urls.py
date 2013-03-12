from django.conf.urls.defaults import *

urlpatterns = patterns(
    'webpay.views',
    url(r'^$', 'compra_webpay', name="webpay-normal"),
)