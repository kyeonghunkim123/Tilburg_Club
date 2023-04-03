from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
# Create your views here.

def mainpage(request):
    return render(request, "user/main.html")

def login(request):
    return render(request, "user/login.html")

def join(request):
    return render(request, "user/join_membership.html")

def logout(request):
    django_logout(request)
    return redirect("/")
