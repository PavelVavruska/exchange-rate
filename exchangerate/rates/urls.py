from django.conf.urls import patterns, url
from rates.models import ExchangeRate

from rates import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<pk>\d{1,2})/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[^\.]+)/$', views.DetailView.as_view(), name='detail1'),
)