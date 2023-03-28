from django.shortcuts import render

# Create your views here.

def mainpage(request):
    return render(request, "user/main.html")

def find_pw(request):
    return render(request, "user/find_pw.html")
