from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from userhandler.models import User
from .models import TextChannel, Server

# Create your views here.


def index(request, pk):
    print('hey')
    return HttpResponse(request, 'Hey!')


@login_required(login_url='login')
def server(request, pk):
    friends = request.user.objects.values('friend_list').distinct()
    textChannel = TextChannel.objects.get(id=pk)
    text_channels = textChannel.parent.text_channels
    context = {'friends': friends, 'text_channels': text_channels, }

    return render(request, 'app/server.html', context)


@login_required(login_url='login')
def friends(request):
    user = User.objects.get(email=request.user.email)
    userFriendList = user.friendlist.all()
    blocked_users = user.blocked_users.all()
    pending = []
    friends = []

    # Checks if the person is blocked, friends or only a one sided friend relationship meaning pending.
    for people in userFriendList:
        if people in blocked_users:
            pass
        elif not user in people.friend.all():
            pending.append(people)
        else:
            friends.append(people)

    context = {
        'friends': friends,
        'blocked': blocked_users,
        'pending': pending,
    }
    return render(request, 'app/friends.html', context)
