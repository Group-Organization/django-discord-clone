from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from userhandler.models import User

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
    userFriendList = user.friend.all()
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
