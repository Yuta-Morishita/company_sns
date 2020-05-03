from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


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
            return redirect('signup')
        else:
            return redirect('login')

    return render(request, 'boardapp/login.html')
