from django.shortcuts import render, redirect
from app01 import models
# Create your views here.


def login(request):
    username = request.POST.get("username")
    pwd = request.POST.get("pwd")
    if models.UserInfo.objects.filter(name=username, pwd=pwd):
        request.session['user'] = {'username': username}
        return redirect("/meeting_list/")

    return render(request, "login.html")


def meeting_list(request):
    return render(request, "meeting_list.html")