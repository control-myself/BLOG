import json
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from blog.apps.account.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import redirect


def author_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(request.POST)
    if request.method == 'POST':
        user = User.objects.filter(email=username, password=password).first()
        if user:
            if user.user_type == 'author':
                login(request, user)
                next = request.GET.get('next')
                if next:
                    return redirect(next)
                return redirect('/profile/')
        
        return HttpResponse(json.dumps({'status': 'error', 'error_message': {'content': '该账号不匹配，点击确认跳转至博客首页！'}}),
                                    content_type='application/json')
    return render(request, "login.html")


def author_logout(request):
    user = request.user
    logout(request)

    url = reverse('article:home')
    return redirect(url)


def profile(request):
    user = request.user
    author_data = {}
    author_data['author'] = user
    return render(request, 'profile.html', {'author_data': author_data})
