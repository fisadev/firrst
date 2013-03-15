#coding: utf-8
from django.conf.urls import patterns, url


urlpatterns = patterns('app.ajax_views',
    url(r'^update_feeds/$', 'update_feeds', name='update_feeds'),
)
