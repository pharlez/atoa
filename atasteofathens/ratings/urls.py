from django.conf.urls import patterns, include, url

urlpatterns = patterns('atasteofathens.ratings.views',
        url(r'^$', 'index'),
        url(r'^users/$', 'users'),
        url(r'^user/(?P<user_name>\S+)/rate/$', 'user_rate'),
        url(r'^user/(?P<user_name>\S+)/$', 'user_profile'),
        url(r'^restaurants/$', 'items'),
)
