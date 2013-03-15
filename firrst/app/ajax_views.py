#coding: utf-8
from models import Feed


def update_feeds(request):
    for f in Feed.objects.all():
        f.update_posts()
