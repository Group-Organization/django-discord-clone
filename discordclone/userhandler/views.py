import random
from django.contrib import messages
from .forms import UserForm
from .models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q


def registerUser(request):
    form = UserForm()

    # Redirects user to profile page if they're trying to login while already logged in.
    if request.user.is_authenticated:
        messages.error(request, 'You are already authenticated!')
        return redirect('profile', request.user.username, request.user.tag)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save(commit=False)

            def userTagGen():
                tag = ''
                for i in range(4):
                    tag += str(random.randint(0, 9))
                return int(tag)
            userTag = userTagGen()

            if User.objects.filter(username=user.username).exists():
                messages.error(request, 'User already exists!')
                return redirect('register')

            # Attempts to get the user a unique tag that hasnt been taken by the username.
            chances = 0
            while User.objects.filter(Q(username=user.username.lower()) and Q(tag=userTag)):
                for i in range(4):
                    userTag = userTagGen()
                    chances = chances + 1
                if chances > 3:
                    messages.error(request, 'Pick another username!')
                    return redirect('register')

            user.username = user.username.lower()
            user.tag = userTag
            user.email = user.email.lower()
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'An error ocurred during registration')
            return redirect('register')

    context = {
        'form': form,
    }

    return render(request, 'userhandler/register.html', context)


def loginUser(request):
    form = UserForm()

    # Redirects user to profile page if they're trying to login while already logged in.
    if request.user.is_authenticated:
        messages.error(request, 'You are already authenticated!')
        return redirect('profile', request.user.username, request.user.tag)

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        print(request.POST)
        if not User.objects.filter(email=email).exists():
            messages.error(request, 'Username not found')
            print(request.POST)
            return redirect('login')

        user = authenticate(request, email=email, password=password)
        if user != None:
            login(request, user)
            print(request.POST)
            return redirect('profile', request.user.username, request.user.tag)
        else:
            messages.error(request, 'Username or password does not exist')

    context = {
        'form': form,
    }

    return render(request, 'userhandler/login.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('home')


def profile(request, username, tag):

    try:
        user = User.objects.filter(Q(username=username) and Q(tag=tag))[0]
    except IndexError:
        messages.error(request, 'User does not exist!')
        return redirect('home')
        # Need to change this later incase the user isn't logged in

    context = {
        'user': user,
    }
    return render(request, 'userhandler/profile.html', context)
