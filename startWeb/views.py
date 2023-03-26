from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import pymysql
# Create your views here.
from django.http import HttpResponse

print('여기는 views.py 파일')

def main(request):
    print('여기는 views.py 파일 line 9')
	# main함수가 실행되면 test.html파일이 열리도록 render
    print('localhost:8080 뒤에 아무것도 없을때 실행')
    return render(request, 'startWeb/test22.html')

def hello1(request):
    print('여기는 views.py 파일 line 14')
    # hello1함수가 실행되면 변수 contents에 저장된 html 코드가 웹에 적용
    contents = '<h1>Hello1</h1>'
    return HttpResponse(contents, content_type='text/html; charset=utf-8')

def index(request):
    print('여기는 views.py 파일 line 21')
    return render(request, "index.html", {})


def join(request):
    print('여기는 views.py 파일 line 27')
    return render(request, "user/join.html", {})

def login(request):
    print('여기는 views.py 파일 line 31')
    return render(request, "user/login.html", {})

@csrf_exempt
def loginSubmit(request):
    dict1 = {}

    id = ""
    pw = ""

    if request.method == 'POST':
        print("리퀘스트 로그" + str(request.body))
        id = request.POST.get('userid','')
        pw = request.POST.get('userpw', '')
        print("id = " + id + " pw = " + pw)

    print('여기는 views.py 파일 line 41')
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='insa', charset='utf8')
    cur = conn.cursor()
    sql = 'select * from userTable'
    vals = ()
    result_validation = False
    cur.execute(sql)
    for row in cur:
        print(row[0], row[1], row[2], row[3], row[4])
        if (id == row[1]) and (pw == row[2]):
            dict1 = {'id': id, 'pw': pw}
            result_validation = True


    # loginSubmit가 실행되면 변수 contents에 저장된 html 코드가 웹에 적용

    contents = ""

    if result_validation:
        print("로그인 성공!")
        contents = '<h1>' + id + '님이 로그인 하였습니다. </h1>'
        return HttpResponse(contents, content_type='text/html; charset=utf-8')
    else:
        print("로그인 실패")
        contents = '<h1> 해당하는 계정이 없습니다 </h1>'
        return HttpResponse(contents, content_type='text/html; charset=utf-8', status=200)

    # if result_validation:
    #     print("로그인 성공!")
    #     return HttpResponse(status=200)
    # else:
    #     print("로그인 실패")
    #     return HttpResponse(status=401)

