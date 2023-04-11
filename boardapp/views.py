from django.shortcuts import render, redirect
from mysql.connector import cursor
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

    request.session['title']=board_title

    print(request.session['title'])
    return render(request, "board/board.html")

