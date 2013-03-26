from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'webpay.views',
    url(r'^$', 'compra_webpay', name="comprawebpay"),
)