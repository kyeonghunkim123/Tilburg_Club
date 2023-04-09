from django.shortcuts import render, redirect
from mysql.connector import cursor
import pymysql

# Create your views here.
def board(request):
    return render(request, "board/board.html")

def board_write(request):
    return render(request, "board/board_write.html")
def board_portfolio(request):
    return render(request, "board/board_portfolio.html")
def board_list(request):

    filename="C:/tilburg_club/tilburg.txt"
    with open(filename) as f:
        root_ps=f.read()
    print(root_ps)
    print(filename)
    dev_ps=root_ps+'dev'

    conn = pymysql.connect(host='130.162.154.239', user='dev', password=dev_ps, db='tilburg_club', charset='utf8')
    cur = conn.cursor()
    sql_select = "select * from board" #where borad = (%s) and 한페이지?
    cur.execute(sql_select)

    for row in cursor.fetchall():
        print(row)

    conn.close()

