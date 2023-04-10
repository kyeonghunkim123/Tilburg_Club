from django.shortcuts import render, redirect
from mysql.connector import cursor
import pymysql

# Create your views here.
def board(request):
    print("------------------------")
    print(request.session['user_id'])
    return render(request, "board/board.html")

def board_write(request):
    return render(request, "board/board_write.html")
def board_list(request):
    conn = pymysql.connect(host='130.162.154.239', user='dev', password='1234', db='tilburg_club', charset='utf8')
    cur = conn.cursor()
    sql_select = "select * from board" #where borad = (%s) and 한페이지?
    cur.execute(sql_select)

    for row in cursor.fetchall():
        print(row)

    conn.close()

