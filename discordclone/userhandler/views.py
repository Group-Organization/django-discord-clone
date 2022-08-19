from django.contrib import messages
from .forms import UserForm
from .models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def registerUser(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)

            if User.objects.filter(username=user.username).exists():
                messages.error(request, 'User already exists!')
                return redirect('register')

            user.username = user.username.lower()
            user.email = user.email.lower()
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error ocurred during registration')
            return redirect('register')

    context = {
        'form': form
        }

    return render(request, 'userhandler/register.html', context)


def loginUser(request):
    form = UserForm()

    # Redirects user to profile page if they're trying to login while already logged in.
    if request.user.is_authenticated:
        messages.error(request, 'You are already authenticated!')
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Username not found')
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username or password does not exist')

    context = {
        'form': form,
    }

    return render(request, 'userhandler/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def profile(request, username):
    user = User.objects.get(username=username)
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
