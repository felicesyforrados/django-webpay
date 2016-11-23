try:
    from django.conf.urls.defaults import url
except ImportError:
    from django.conf.urls import url

from .views import compra_webpay

urlpatterns = patterns(
    url(r'^$', compra_webpay, name="comprawebpay"),
)
