import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, authenticate, logout  
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Profile
from .forms import registerForm
from feeds.models import Feed

def request_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'Successful Logged In')
            return redirect('feeds')
        messages.error(request, 'Username or password is Incorrect!')
        return redirect('login')
    
    return render(request,  'userauth/auth.html')


def register_request(request):
   
    if request.method == 'POST':
        form = registerForm(request.POST)
        print(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            role  = request.POST['role']
            if User.objects.filter(email=email).exists():
                messages.error(request,'User with this email already exists, Use a different email!!')
                return redirect('register')
            else:
                user = form.save()
                login(request, user)
                profile = Profile.objects.get(user=request.user)
                profile.role = role
                profile.save()
                messages.success(request, "Successful Registered!")
                if 'next' in request.POST:
                   return redirect(request.POST.get('next'))
                return redirect('feeds')
        
    else:
        form = registerForm()
    context = {
        'form':form
    }
    return render(request, 'userauth/auth.html', context )




def logout_request(request):
    logout(request)
    messages.success(request,f"Logged out successful")
    return redirect('login')



def timeline(request, user):
    profile = Profile.objects.get(user=user)
    follows = Profile.objects.filter(user=user).values('followers').count()
    
    feeds = Feed.objects.filter(user=user)
    context = {
        'data':profile,
        'feeds':feeds,
        'follows':follows
    }
    return render(request, 'userauth/timeline.html', context)





def follow(request):
    if request.method == 'POST':
        profile= get_object_or_404(Profile, id=request.POST.get('id'))
        is_followed = False
        if profile.followers.filter(id=request.user.id).exists():
            profile.followers.remove(request.user)
            is_followed = False
        else:
            profile.followers.add(request.user)
            is_followed = True

        followers_count = profile.followers.all().count()
        response_data = {}
        response_data['result'] = 'Successfull followed'
        response_data['is_followed']= is_followed
        response_data['the_id'] = profile.id
        response_data['count'] = followers_count
        return HttpResponse(
            json.dumps(response_data),
            content_type='applicatin/json'
        )
    else:
        return HttpResponse(
            json.dumps({'Error':'Faild to submit'}),
            content_type = "application/json"
        )



def officers(request):
    officers = Profile.objects.filter(role='officer')
    context = {
        'officers':officers
    }
    return render(request, 'userauth/officers.html', context)