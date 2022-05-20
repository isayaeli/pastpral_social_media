from django.shortcuts import render
from .models import Feed
# Create your views here.
def feeds(request):
    feeds = Feed.objects.all()
    context = {
        'feeds':feeds
    }
    return render(request, 'feeds/feeds.html',context)