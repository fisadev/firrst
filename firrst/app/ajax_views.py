#coding: utf-8
from django.shortcuts import render_to_response

from models import Feed


def update_feeds(request):
    for f in Feed.objects.all():
        f.update_posts()

def get_sidebar(request):
    return render_to_response('ajax/sidebar.html',
                              {'feeds': Feed.objects.all()})
