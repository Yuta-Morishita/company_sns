from django.shortcuts import render
from django.contrib.auth.models import User


def signupfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username, '', password)
        return render(request, 'boardapp/signup.html', {'some': 100})
    return render(request, 'boardapp/signup.html', {'some': 100})
