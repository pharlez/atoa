from django.conf.urls import patterns, include, url

urlpatterns = patterns(
        'atasteofathens.spots.views',
        url(r'^$', 'index'),
        #url(r'^users/$', 'users'),
        #url(r'^user/(?P<user_name>\S+)/rate/$', 'user_rate'),
        #url(r'^user/(?P<user_name>\S+)/$', 'user_profile'),
        #url(r'^restaurant/(?P<restaurant_slug>\S+)/$', 'restaurant_profile'),
        url(r'^restaurants/$', 'restaurants'),
)
