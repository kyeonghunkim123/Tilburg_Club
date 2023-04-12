from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
# from mysql.connector import cursor
import pymysql

# Create your views here.
def board(request):
    print("------------------------")
    # print(request.session['title'])
    return render(request, "board/board.html")

def board_write(request):
    return render(request, "board/board_write.html")
def board_list(request):
    filename = "C:/tilburg_club/tilburg.txt"
    with open(filename) as f:
        root_ps = f.read().strip()
    dev_ps = root_ps + 'dev'
    print(dev_ps)
    print(root_ps)

    conn = pymysql.connect(host='130.162.154.239', user='dev', password=dev_ps, db='tilburg_club', charset='utf8')
    cur = conn.cursor()
    sql_select = "select * from board_table"
    cur.execute(sql_select)

    for row in cur.fetchall():
        print(row)

    conn.close()

def board_reg(request):
    board_title=request.POST.get("title")
    board_nickname = request.POST.get("nickname")
    board_content = request.POST.get("content")

    filename = "C:/tilburg_club/tilburg.txt"
    with open(filename) as f:
        root_ps = f.read().strip()
    dev_ps = root_ps + 'dev'

    conn = pymysql.connect(host='130.162.154.239', user='dev', password=dev_ps, db='tilburg_club', charset='utf8')
    print(root_ps)
    cur = conn.cursor()

    sql_insert = 'insert into board_table (title, content, nickname) values(%s,%s,%s)'
    val = (board_title, board_nickname, board_content)
    cur.execute(sql_insert, val)
    conn.commit()
    conn.close()

    request.session['title', 'content', 'nickname'] = board_title

    print(request.session['title'])
    return render(request, "board/board.html")

def board_list(request):
    return render(request, "board/board_list.html")








# -- 2023.04.12. KKH 추가 시작 --

class BoardClass:
    def __init__(self, bno, title, content, writer, regDate, updateDate):
        self.bno = bno
        self.title = title
        self.content = content
        self.writer = writer
        self.regDate = regDate
        self.updateDate = updateDate

def h_list(request):
    filename = "C:/tilburg_club/tilburg.txt"
    with open(filename) as f:
        root_ps = f.read().strip()
    dev_ps = root_ps + 'dev'
    print(dev_ps)

    conn = pymysql.connect(host='130.162.154.239', user='dev', password=dev_ps, db='tilburg_club', charset='utf8')
    # conn = pymysql.connect(host='localhost', user='root', password='1234', db='tilburg_club', charset='utf8')
    cur = conn.cursor()
    sql_select = "select bno, title, content, writer, DATE_FORMAT(regDate, '%Y%m%d%H%i%s'), DATE_FORMAT(updateDate, '%Y%m%d%H%i%s') from TBL_BOARD ORDER BY bno desc LIMIT 10 OFFSET 10"
    cur.execute(sql_select)
    rows = cur.fetchall()
    list1 = []
    for row in rows:
        boardClass = BoardClass(row[0],row[1],row[2],row[3],row[4],row[5])
        list1.append(boardClass)
    # request.session['list'] = list1
    # print(rows)
    context = {'board_list': list1}
    return render(request, 'board/h_list.html', context)

def h_register_get(request):
    print("---------GET 1 --------")
    return render(request, 'board/h_register.html')
# @require_http_methods(['GET'])
# def h_register_get(request):
#     print("---------GET 1 --------")
#     return render(request, 'board/h_register.html')

@require_http_methods(['POST'])
def h_register_post(request):
    print("---------POST 2 --------")
    # 아래 수정해야함.
    return render(request, 'board/h_register.html')


def h_modify(request):
    return render(request, 'board/h_modify.html')

    # -- 2023.04.12. KKH 추가 끝 --
