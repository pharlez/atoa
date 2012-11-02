from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'atasteofathens.spots.views.index'),
    url(r'^spots/', include('atasteofathens.spots.urls')),
    url(r'^accounts/', include('atasteofathens.accounts.urls')),
    url(r'^accounts/', include('atasteofathens.registration.urls')),
    url(r'^admin/', include(admin.site.urls))
)
