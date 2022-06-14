
import json
from .models import Comment
from django.http import HttpResponse
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



def feed_details(request ,id):
    feed =  get_object_or_404(Feed, id=id)
    if request.method == "POST":
        content = request.POST['content']
        user = request.user
        # response_data = {}
        comment =  Comment(content=content, feed=feed, user=user)
        comment.save()
        return redirect('feed_details', id=id)
        # response_data['result'] = "Comment Added"
        # response_data['user'] = user.username
        # response_data['comment'] = content
        # return HttpResponse(
        #     json.dumps(response_data),
        #     content_type = 'Application/json'
        # )
 

    context = {
        'data':feed
    }
    return render(request,'feeds/details.html', context)


def edit_feed(request ,id):
    feed =  get_object_or_404(Feed, id=id)
    if request.method == 'POST':
        feed.user = request.user
        feed.texts = request.POST['texts']
        if 'image' in request.FILES:
            feed.image = request.FILES.get('image')
        if 'video' in request.FILES:
            feed.video = request.FILES.get('video')
        feed.save()
        return redirect('feeds')
    context = {
        'data':feed
    }
    return render(request, 'feeds/feed_edit.html',context)

def delete_feed(request, id):
    feed =  get_object_or_404(Feed, id=id)
    feed.delete()
    messages.success(request, 'Post has been deleted!')
    return redirect('feeds')



