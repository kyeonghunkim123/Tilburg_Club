from django.shortcuts import render
import pymysql

# Create your views here.
def board(request):
    return render(request,  "board/board.html")

def board_list(request):

    conn = pymysql.connect(host='130.162.154.239', user='dev', password='1234', db='tilburg_club', charset='utf8')
    cur = conn.cursor()
    sql_select = "SELECT * from board" #where ??
    cur.execute(sql_select)

    for row in cursor.fetchall():
        print(row)

    conn.close()

def write(request):
    return render(request,  "write_form/board.html")