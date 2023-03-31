from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import pymysql

# Create your views here.

def mainpage(request):
    return render(request, "user/main.html")

def login(request):
    return render(request, "user/login.html")

def join(request):
    return render(request, "user/join_membership.html")

def logout(request):
    return HttpResponse("로그아웃 페이지입니다.")

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
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='tilburg_club', charset='utf8')
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
    #return render(request, "user/find_mp.html")
