#coding: utf-8
from django.conf.urls import patterns, url


urlpatterns = patterns('app.ajax_views',
    url(r'^get_sidebar/$', 'get_sidebar', name='get_sidebar'),
    url(r'^get_feed/(?P<feed_id>\d+)/$', 'get_feed', name='get_feed'),
    url(r'^update_feeds/$', 'update_feeds', name='update_feeds'),
)
