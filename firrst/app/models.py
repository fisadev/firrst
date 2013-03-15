from django.db import models


class Feed(models.Model):
    name = models.CharField(max_length=255)
    url = models.TextField()
    last_fetch = models.DateTimeField()


class Post(models.Model):
    feed = models.ForeignKey(Feed)
    fetched_at = models.DateTimeField()
    read = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    content = models.TextField()
