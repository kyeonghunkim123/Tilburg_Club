from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
import pymysql

# Create your views here.

def mainpage(request):
    return render(request, "user/main.html")

def login(request):
    return render(request, "user/login.html")

def join(request):
    return render(request, "user/join_membership.html")

def logout(request):
    auth_logout(request)
    return redirect('/')

def find_pw(request):
    return render(request, "user/find_pw.html")

def find_mp(request):

    str_name = request.GET.get("username")
    str_phone = request.GET.get("phone")
    print('=============1111111==================')
    if (str_name == "") or (str_phone == ""):
        return HttpResponseRedirect("find_pw")

    print('===============================')
    print(str_name,str_phone)
    print('===============================')
    #conn = pymysql.connect(host='localhost', user='root', password='1234', db='tilburg_club', charset='utf8')
    conn = pymysql.connect(host='130.162.154.239', user='dev', password='1234', db='tilburg_club', charset='utf8')
    cur = conn.cursor()
    print('2')
    sql_select = 'select password from userTable where username = (%s) and phone = (%s)'
    val = (str_name, str_phone)
    cur.execute(sql_select, val)

    print('3')
    row = cur.fetchone()
    str_password = row[0]
    print('4')

    content = f"<h1>{str_password} is your password</h1>"

    if (row == None):
        return render(request, "user/find_pw.html")
    print('5')
    return HttpResponse(content)

    # if (str_name != "username") or (str_phone != "phone"):
    #     return render(request, "user/find_pw.html")
    # print('6')
    #return render(request, "user/find_mp.html")
