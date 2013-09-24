from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$',
        views.IndexView.as_view(),
        name='index'),
    url(r'^(?P<year>\d{4})/$',
        views.IndexView.as_view(),
        name='year'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$',
        views.IndexView.as_view(),
        name='month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$',
        views.IndexView.as_view(),
        name='day'),
    url(r'^(?P<slug>[^\.]+)/$',
        views.DetailView.as_view(),
        name='detail'),
)