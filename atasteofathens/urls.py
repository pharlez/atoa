from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'atasteofathens.ratings.views.index'),
    url(r'^ratings/', include('atasteofathens.ratings.urls')),
    url(r'^accounts/', include('atasteofathens.accounts.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
