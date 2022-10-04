from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from userhandler.models import User
from django.contrib import messages
from .forms import ServerMessageForm
from .models import TextChannel, Server, ServerMessage
from django.views.decorators.http import require_http_methods
from .serializer import *
from django.db.models import Q


# Create your views here.


def index(request, channelId):
    return HttpResponse(request, TextChannel.objects.get(id=channelId))


@login_required(login_url='login')
def server(request, serverId, channelId):
    user = User.objects.all().filter(id=request.user.id, tag=request.user.tag).first()
    friends = User.objects.all().filter(id=user.id).first().friends.all()
    server = Server.objects.get(id=serverId)
    textChannel = TextChannel.objects.get(id=channelId)
    text_channels = TextChannel.objects.all().filter(server=server)
    server_messages = ServerMessage.objects.all().filter(server=server)
    # Voice channels query needed and stuff
    form = ServerMessageForm()

    if request.method == 'POST':
        form = ServerMessageForm(request.POST)
        if form.is_valid():
            server_msg = form.save(commit=False)
            server_msg.user = user
            server_msg.server = server
            server_msg.channel = textChannel
            form.save()

    context = {'friends': friends,
               'text_channels': text_channels,
               'textChannel': textChannel,
               'server_messages': server_messages,
               'form': form}

    return render(request, 'app/server.html', context)


@require_http_methods(["GET"])
@login_required(login_url='login')
def friends(request):
    try:
        mode = request.GET['mode']
        user = User.objects.get(email=request.user.email)
    except:
        return JsonResponse({'err': 'Mode is not specified'}, status=404)

    if mode == 'friends':
        response = user.friends.all()
    elif mode == 'pending':
        response = user.pending.all()
    elif mode == 'blocked':
        response = user.blocked.all()
    elif mode == 'requests':
        response = User.objects.filter(pending=request.user)
    elif mode == 'online':
        response = User.objects.filter(
            Q(friends=request.user) & Q(status='online'))
    else:
        return JsonResponse({'err': 'Mode not supported'}, status=400)

    serializer = UserSerializer(response, many=True)

    return JsonResponse(serializer.data, safe=False, status=200)


@require_http_methods(['GET'])
@login_required(login_url='login')
def search(request):
    try:
        q = request.GET['q'] # If there is no q, it returns all the user's friends.
    except:
        q = ''
    
    response = User.objects.filter(Q(friends=request.user) & (Q(username__contains=q) | Q(tag__contains=q)))
    serializer = UserSerializer(response, many=True)
    return JsonResponse(serializer.data, status=200, safe=False)


@login_required(login_url='login')
def addFriend(request):
    try:
        username = request.GET['username'].lower()
        tag = int(request.GET['tag'])
        friend = User.objects.filter(username=username, tag=tag)[0]
    except:
        messages.error(request, 'User does not exist')
        return redirect('home')

    userFriends = request.user.friends.all()
    userPending = request.user.pending.all()
    userBlocked = request.user.blocked.all()

    # Trying to add yourself
    if request.user == friend:
        messages.error(request, 'You can\'t add yourself!')
        return redirect('home')

    # If the user is already friends with the active user.
    if friend in userFriends or friend in userPending:
        messages.error(request, 'You\'ve already added this user!')
        return redirect('home')

    # If the active user has blocked the user.
    elif friend in userBlocked:
        messages.error(request, 'You\'ve blocked this user!')
        return redirect('home')

    elif request.user in friend.blocked.all():
        messages.error(request, 'This user has blocked you!')
        return redirect('home')

    # If the user being friended is already friends(pending) with the active user, it makes both user friends, and removes the pending status from the user being friended.
    if request.user in friend.pending.all():
        request.user.friends.add(friend)
        friend.pending.remove(request.user)
        friend.friends.add(request.user)
    else:  # If the user being friended is not friends with the active user, it adds the active user to the pending list.
        request.user.pending.add(friend)

    messages.success(request, 'Your friend was added successfully!')
    return redirect('home')


def removeFriend(request):
    try:
        username = request.GET['username'].lower()
        tag = int(request.GET['tag'])
        friend = User.objects.filter(username=username, tag=tag)[0]
    except:
        messages.error(request, 'User does not exist')
        return redirect('home')

    userFriends = request.user.friends.all()
    userPending = request.user.pending.all()
    userBlocked = request.user.blocked.all()

    # Trying to unfriend yourself.
    if request.user == friend:
        messages.error(request, 'You can\'t unfriend yourself!')
        return redirect('home')

    # Trying to unfriend someone who is not friends with the user.
    # friends are either pending or friends hence checking for both.
    if not (friend in userFriends or friend in userPending):
        messages.error(request, 'You are not friends with this user!')
        return redirect('home')

    # If the user is friends with the active user it unfriends them, and add the pending status to the user since the active user has unfriended them.
    if friend in userFriends:
        request.user.friends.remove(friend)
        friend.friends.remove(request.user)
        friend.pending.add(request.user)
    # Just removes the user from pending since, the other user has no relationship with the active user.
    elif friend in userPending:
        request.user.pending.remove(friend)

    return redirect('home')


def blockUser(request):
    try:
        username = request.GET['username'].lower()
        tag = int(request.GET['tag'])
        user = User.objects.filter(username=username, tag=tag)[0]
    except:
        messages.error(request, 'User does not exist')
        return redirect('home')

    userFriends = request.user.friends.all()
    userPending = request.user.pending.all()
    userBlocked = request.user.blocked.all()

    # Trying to block yourself.
    if request.user == user:
        messages.error(request, 'You can\'t block yourself!')
        return redirect('home')

    # If the user is already blocked
    if user in userBlocked:
        messages.error(request, 'You\'ve already blocked this user!')
        return redirect('home')

    # Blocks the user, and if the active user is friends with the user being blocked, the user being blocked friend status would be changed to pending.
    if user in userFriends:
        request.user.friends.remove(user)
        user.friends.remove(request.user)
        user.pending.add(request.user)
    elif user in userPending:
        request.user.pending.remove(user)

    request.user.blocked.add(user)

    return redirect('home')


def home(request):
    return render(request, 'app/home.html')


def unblockUser(request):
    try:
        username = request.GET['username'].lower()
        tag = int(request.GET['tag'])
        user = User.objects.filter(username=username, tag=tag)[0]
    except:
        messages.error(request, 'User does not exist')
        return redirect('home')

    userFriends = request.user.friends.all()
    userPending = request.user.pending.all()
    userBlocked = request.user.blocked.all()

    # Trying to unblock yourself.
    if request.user == user:
        messages.error(request, 'You can\'t unblock yourself!')
        return redirect('home')

    # If the user is not blocked.
    if not user in userBlocked:
        messages.error(request, 'This user is not blocked!')
        return redirect('home')

    request.user.blocked.remove(user)

    return redirect('home')


def room(request, room_name):
    return render(request, 'app/testRoom.html', {
        'room_name': room_name
    })


def rooms(request):
    return render(request, 'app/test.html')
