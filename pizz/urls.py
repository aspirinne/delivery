from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *


app_name = 'pizz'


urlpatterns = [
    url(r'^$', api_root),
    url(r'^orders/$', OrderList.as_view(), name='order-list'),
    url(r'^orders/(?P<pk>\d+)/$', OrderDetail.as_view(), name='order-detail'),
    url(r'^pizzas/$', PizzaList.as_view(), name='pizza-list'),
    url(r'^pizzas/(?P<pk>\d+)/$', PizzaDetail.as_view(), name='pizza-detail'),
    url(r'^customers/$', CustomerList.as_view(), name='customer-list'),
    url(r'^customers/(?P<pk>\d+)/$', CustomerDetail.as_view(), name='customer-detail'),
]


# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
