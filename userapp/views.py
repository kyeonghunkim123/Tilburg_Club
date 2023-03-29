from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mainpage(request):
    return render(request, "user/main.html")

def login(request):
    return render(request, "user/login.html")

def join(request):
    return render(request, "user/join_membership.html")

def logout(request):
    return HttpResponse("로그아웃 페이지입니다.")