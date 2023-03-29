from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def mainpage(request):
    return render(request, "user/main.html")

def login(request):
    return render(request, "user/login.html")

def logout(request):
    return HttpResponse('로그아웃 페이지입니다.')