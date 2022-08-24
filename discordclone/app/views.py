from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from userhandler.models import User
from django.contrib import messages

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
    friends = user.friendlist.all()
    blocked_users = user.blocked_users.all()
    pending = user.pending_users.all()

    for people in friends:
        if people in blocked_users:
            user.friendlist.remove(people)
        elif not user in people.friendlist.all():
            user.friendlist.remove(people)
            user.pending_users.add(people)

    context = {
        'friends': friends,
        'blocked': blocked_users,
        'pending': pending,
    }
    return render(request, 'app/friends.html', context)


@login_required(login_url='login')
def addFriend(request, friendUsername, friendTag):
    newFriend = User.objects.filter(username=friendUsername.lower())
    user = request.user
    userFriends = user.friendlist.all()

    if request.user == newFriend:
        messages.error(request, 'You can\'t add yourself!')
        return redirect('friends')

    if not newFriend.exists():
        messages.error('User does not exist!')
        return redirect('friends')
    if newFriend[0] in userFriends:
        messages.error(request, 'You\'ve already added this user!')
        return redirect('friends')

    print(newFriend[0])
    user.friendlist.add(newFriend[0])

    return redirect('friends')


def removeFriend(request, friendUsername, friendTag):
    friend = User.objects.filter(username=friendUsername.lower())
    user = request.user
    userFriends = user.friendlist.all()
    userPendingFriends = user.pending_users.all()

    if request.user == friend:
        messages.error(request, 'You can\'t unfriend yourself!')
        return redirect('friends')

    if not friend.exists():
        messages.error('User does not exist!')
        return redirect('friends')
    if not friend[0] in userFriends or not friend[0] in userPendingFriends:
        print(userPendingFriends, userFriends)
        messages.error(request, 'You are not friends with this user!')
        return redirect('friends')

    if friend[0] in userFriends:
        user.friendlist.remove(friend[0])
    elif friend[0] in userPendingFriends:
        user.pending_users.remove(friend[0])

    return redirect('friends')
