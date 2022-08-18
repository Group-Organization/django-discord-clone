from django.contrib import messages
from .forms import UserForm
from .models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import django
django.setup()


def registerUser(request):
    page = 'register'
    form = UserForm()
    context = {'page': page, 'form': form}

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            return messages.error(request, 'An error ocurred during registration')
    return render(request, 'userhandler/register_login.html', context)


def loginUser(request):
    page = 'login'
    context = {'page': page}

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)

        except:
            messages.error(request, 'Username not found')

        user = authenticate(request, username=username, password=password)

        if user != None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')

    return render(request, 'userhandler/register_login.html', context)


def profile(request, pk):
    user = User.objects.get(id=pk)
    context = {
        'user': user,
    }
    return render(request, 'userhandler/profile.html', context)


def profiles(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'userhandler/profiles.html', context)
