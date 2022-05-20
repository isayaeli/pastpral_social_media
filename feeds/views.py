from django.shortcuts import render
from .models import Feed
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login')
def feeds(request):
    feeds = Feed.objects.all().order_by('-id')
    context = {
        'feeds':feeds
    }
    return render(request, 'feeds/feeds.html',context)