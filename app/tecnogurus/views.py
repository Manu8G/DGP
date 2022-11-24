from django.shortcuts import render
from .models import Profile, Friend

def index(request):
    user = request.user.profile
    friends = user.friends.all()
    context = {"user": user, "friends": friends}
    return render(request, 'tecnogurus/index.html', context)

def detail(request,pk):
    friend = Friend.object.get(profile_id=pk)
    context = {"friend": friend}
    return render(request, "tecnogurus/detail.html", context)