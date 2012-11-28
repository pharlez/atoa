from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'atasteofathens.spots.views.index'),
    url(r'^spots/', include('atasteofathens.spots.urls')),
    url(r'^accounts/', include('atasteofathens.accounts.urls')),
)
