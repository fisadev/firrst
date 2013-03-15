# Create your views here.
from django.shortcuts import render

from models import Feed


def home(request):
    return render(request, 'home.html', {})

def update_feeds(request):
    for f in Feed.objects.all():
        f.update_posts()
