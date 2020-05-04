from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import Board
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy


def signupfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request, 'boardapp/signup.html', {'error': 'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(username2, '', password2)
            return render(request, 'boardapp/signup.html', {'some': 100})
    return render(request, 'boardapp/signup.html', {'some': 100})


def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)

        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')

    return render(request, 'boardapp/login.html')


@login_required
def listfunc(request):
    object_list = Board.objects.all()
    return render(request, 'boardapp/list.html', {'object_list': object_list})


def logoutfunc(request):
    logout(request)
    return redirect('login')


def detailfunc(request, pk):
    object = Board.objects.get(pk=pk)
    return render(request, 'boardapp/detail.html', {'object': object})


def goodfunc(request, pk):
    post = Board.objects.get(pk=pk)
    post.good = post.good + 1
    post.save()
    return redirect('list')


def readfunc(request, pk):
    post = Board.objects.get(pk=pk)
    post2 = request.user.get_username()
    if post2 in post.readtext:
        return redirect('list')
    else:
        post.read += 1
        post.readtext = post.readtext + ' ' + post2
        post.save()
        return redirect('list')


class CreateView(generic.CreateView):
    template_name = 'boardapp/create.html'
    model = Board
    fields = ('title', 'content', 'author', 'images')
    success_url = reverse_lazy('list')
