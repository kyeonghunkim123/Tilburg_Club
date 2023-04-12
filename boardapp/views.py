from django.shortcuts import render, redirect
from mysql.connector import cursor
import pymysql

# Create your views here.
def board(request):
    print("------------------------")

    return render(request, "board/board.html")

def board_write(request):
    return render(request, "board/board_write.html")
def complete_write(request):
    cmplt_title = request.POST.get("title")
    cmplt_userid = request.POST.get("nickname")
    cmplt_content = request.POST.get("content")

    filename = "C:/tilburg_club/tilburg.txt"
    with open(filename) as f:
        root_ps = f.read().strip()
    dev_ps = root_ps + 'dev'
    print(dev_ps)
    print(root_ps)

    conn = pymysql.connect(host='130.162.154.239', user='dev', password=dev_ps, db='tilburg_club', charset='utf8')
    print(root_ps)
    cur = conn.cursor()
    sql_insert = 'insert into board_table (title, content, nickname, created_at, views) values(%s,%s,%s,%s,%s)'
    val = (cmplt_title, cmplt_userid, cmplt_content)
    cur.execute(sql_insert, val)
    conn.commit()
    conn.close()
    return render(request, "board/board.html")

def board_list(request):
    return render(request, "board/board_list.html")

