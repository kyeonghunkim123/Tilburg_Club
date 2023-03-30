from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mainpage(request):
    return render(request, "user/main.html")

<<<<<<< HEAD
def login(request):
    return render(request, "user/login.html")

def join(request):
    return render(request, "user/join_membership.html")

def logout(request):
    return HttpResponse("로그아웃 페이지입니다.")

def find_pw(request):
    return render(request, "user/find_pw.html")

def find_me(request):

    str_name = request.GET.get("username", )
    str_phone = request.GET.get("phone", )

    conn = pymysql.connect(host='localhost', user='root', password='1234', db='tilburg_club', charset='utf8')
    cur = conn.cursor()

    sql_select = 'select password from userTable where username = (%s) and phone = (%s)'
    val = (str_name, str_phone)
    cur.execute(sql_select, val)

    row1 = cur.fetchone()
    str_password = row1[0]

    content = f"<h1>{str_password} is your password</h1>"
    return HttpResponse(content)
    #return render(request, "user/find_phonenum.html")
=======
def find_pw(request):
    return render(request, "user/find_pw.html")
>>>>>>> 4e73767e5ce74812670625bb780a4d32b452c243
