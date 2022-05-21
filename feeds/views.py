from email import message
from django.shortcuts import get_object_or_404, render, redirect
from .models import Feed
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required(login_url='/login')
def feeds(request):
    feeds = Feed.objects.all().order_by('-id')
    if request.method == 'POST':
        print(request.POST)
        feed = Feed()
        feed.user = request.user
        feed.texts = request.POST['texts']
        feed.image = request.FILES.get('image')
        feed.video = request.FILES.get('video')
        feed.save()

        return redirect('feeds')
    context = {
        'feeds':feeds
    }
    return render(request, 'feeds/feeds.html',context)

def delete_feed(request, id):
    feed =  get_object_or_404(Feed, id=id)
    feed.delete()
    messages.success(request, 'Post has been deleted!')
    return redirect('feeds')