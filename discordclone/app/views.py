from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from userhandler.models import User
from django.contrib import messages


# Create your views here.


def index(request):
    print('hey')
    return HttpResponse(request, 'Hey!')


@login_required(login_url='login')
def server(request):
    # friends = request.user.
    context = {'friends': friends}

    return render(request, 'app/server.html', context)


@login_required(login_url='login')
def friends(request):
    user = User.objects.get(email=request.user.email)
    friends = user.friendlist.all()
    blocked_users = user.blocked_users.all()
    pending = user.pending_users.all()

    context = {
        'friends': friends,
        'blocked': blocked_users,
        'pending': pending,
    }
    return render(request, 'app/friends.html', context)


@login_required(login_url='login')
def addFriend(request, friendUsername):
    newFriend = User.objects.filter(username=friendUsername.lower())
    user = request.user
    userFriends = user.friendlist.all()

    if not newFriend.exists():
        messages.error('User does not exist!')
        return redirect('friends')
    if newFriend[0] in userFriends:
        messages.error(request, 'You\'ve already added this user!')
        return redirect('friends')

    print(newFriend[0])
    user.friendlist.add(newFriend[0])

    return redirect('friends')


def removeFriend(request, friendUsername):
    friend = User.objects.filter(username=friendUsername.lower())
    user = request.user
    userFriends = user.friendlist.all()

    if not friend.exists():
        messages.error('User does not exist!')
        return redirect('friends')
    if not friend[0] in userFriends:
        messages.error(request, 'You are not friends with this user!')
        return redirect('friends')

    user.friendlist.remove(friend[0])
    return redirect('friends')
