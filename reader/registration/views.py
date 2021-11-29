from django.shortcuts import render
from django.contrib.auth import authenticate, login


def login_user(request):
    # username = request.POST['user']
    # password = request.POST['password']
    # user = authenticate(request, username=username, password=password)
    return render(request, 'registration/login_page.html')
