#coding: utf-8
from datetime import datetime
import feedparser

from django.db import models


class Feed(models.Model):
    FETCH_OK = 'ok'
    FETCH_ERROR = 'error'

    name = models.CharField(max_length=255)
    url = models.TextField()
    last_fetch = models.DateTimeField(null=True)
    last_correct_fetch = models.DateTimeField(null=True)
    last_fetch_result = models.CharField(max_length=255, blank=True)
    last_fetch_detail = models.TextField()

    def update_posts(self):
        self.last_fetch = datetime.now()

        try:
            feed = feedparser.parse(self.url)
            items_added = 0

            for item in feed.get('items', []):
                title = item.get('title', '').strip()

                if not Item.objects.filter(feed=self, title=title).exists():
                    Item.objects.create(feed=self,
                                        title=title,
                                        content=item.get('summary', ''),
                                        fetched_at=datetime.now())
                    items_added += 1

            self.last_correct_fetch = datetime.now()
            self.last_fetch_result = Feed.FETCH_OK
            self.last_fetch_detail = '%i new items added' % items_added
        except Exception as err:
            self.last_fetch_result = Feed.FETCH_ERROR
            self.last_fetch_detail = str(err)

        self.save()


class Item(models.Model):
    feed = models.ForeignKey(Feed)
    fetched_at = models.DateTimeField()
    read = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    content = models.TextField()
