from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
import pymysql

# Create your views here.

def mainpage(request):
    return render(request, "user/main.html")

def login(request):
    return render(request, "user/login.html")

def complete_login(request):
    print('=============000==================')

    login_id = request.POST.get("ID")
    login_password = request.POST.get("password")
    print('=============1111111==================')

    print('===============================')
    print(login_id,login_password)
    print('===============================')
    #conn = pymysql.connect(host='localhost', user='root', password='1234', db='tilburg_club', charset='utf8')
    conn = pymysql.connect(host='130.162.154.239', user='dev', password='1234', db='tilburg_club', charset='utf8')
    cur = conn.cursor()
    print('2')
    sql_select = 'select ID,userpassword from main where ID = (%s) and userpassword = (%s)'
    val = (login_id, login_password)
    cur.execute(sql_select, val)
    print('3')
    print(sql_select)


    # if str_name != sql_select:
    #      return render(request, "user/find_pw.html")

    print('3')
    row = cur.fetchone()
    print(row)

    if row is None :
        return render(request, "user/login.html")
    else:
        return render(request, "user/main.html")


    # if str_name !=row[1] or str_phone !=row[2]:
    #     return render(request, "user/find_pw.html")

    # str_password = row[0]


def join(request):
    return render(request, "user/join_membership.html")

def complete_join(request):
    join_name = request.POST.get("name")
    join_phone = request.POST.get("phone")
    join_ID = request.POST.get("ID")
    join_password = request.POST.get("userpassword")
    join_address = request.POST.get("useraddress")

    conn = pymysql.connect(host='130.162.154.239', user='dev', password='1234', db='tilburg_club', charset='utf8')
    cur = conn.cursor()
    sql_insert = 'insert into main (username, phone, userpassword, useraddress,ID) values(%s,%s,%s,%s,%s)'
    val = (join_name, join_phone,join_password,join_address,join_ID)
    cur.execute(sql_insert, val)
    conn.commit()
    conn.close()
    return render(request, "user/main.html")

def logout(request):
    auth_logout(request)
    return redirect('/')

def find_pw(request):
    return render(request, "user/find_pw.html")

def find_mp(request):

    str_ID = request.POST.get("ID")
    str_phone = request.POST.get("phone")

    print('===============================')
    print(str_ID,str_phone)
    print('===============================')
    #conn = pymysql.connect(host='localhost', user='root', password='1234', db='tilburg_club', charset='utf8')
    conn = pymysql.connect(host='130.162.154.239', user='dev', password='1234', db='tilburg_club', charset='utf8')
    cur = conn.cursor()
    print('2')
    sql_select = 'select userpassword from main where ID = (%s) and phone = (%s)'
    val = (str_ID, str_phone)
    a=cur.execute(sql_select, val)
    print('3')
    print(sql_select)
    print(a)

    # if str_name != sql_select:
    #      return render(request, "user/find_pw.html")


    print('3')
    row = cur.fetchone()
    str_password = row[0]


    if row is None :
        return render(request, "user/find_pw.html"
    )
    else:
<<<<<<< HEAD

    content = f"<h1>{str_password} is your password</h1>"
=======
      content = f"<h1>{str_password} is your password</h1>"
>>>>>>> cfe235e2a0d63b01588284469c3f6a0dcd312352

    if (row == None):
        return render(request, "user/find_pw.html")

    print('5')
    return HttpResponse(content)
def board(request):
    return render(request,  "user/board.html")

def find_id(request):
    return render(request, "user/find_id.html")

def get_request(request):
    str_name = request.GET.get('username')
    str_phone = request.GET.get('phone')
    val = (str_name, str_phone)
    conn = pymysql.connect(host='130.162.154.239',
                           user='dev',
                           password='1234',
                           db='tilburg_club',
                           charset='utf8')
    cur = conn.cursor()
    return cur, val

def find_mi(request):
    cur, val = get_request(request)
    print('db done')
    sql_select = 'select ID from main where username = (%s) and phone = (%s)'
    cur.execute(sql_select, val)

    row = cur.fetchone()
    str_id = row[0]

    content = f'<h1>{str_id} is your id</h1>'

    if row == None:
        return render(request, 'user/find_id.html')
    return HttpResponse(content)
