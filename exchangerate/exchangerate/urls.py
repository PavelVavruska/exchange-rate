from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^rates/', include('rates.urls', namespace="rates")),
    url(r'^admin/', include(admin.site.urls)),
)
