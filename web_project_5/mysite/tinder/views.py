from django.shortcuts import render, redirect
from .forms import CreateUserForm, AddPost
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Post


@login_required(login_url='login')
def home(request):
    # Data = {'Data': User.objects.all()}
    Data = {'Data': Post.objects.all()}
    return render(request, 'pages/home.html', Data)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')

        context = {'form': form}
        return render(request, 'pages/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')

        context = {}
        return render(request, 'pages/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def profile(request, id):
    Data = User.objects.get(id=id)
    return render(request, 'pages/profile.html', {'Data': Data})


@login_required(login_url='login')
def addpost(request):
    form = AddPost()
    if request.method == 'POST':
        form = AddPost(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/listpost')
    return render(request, 'pages/addpost.html', {'form': form})


