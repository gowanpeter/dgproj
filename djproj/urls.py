from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^djapp/', include('djapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
