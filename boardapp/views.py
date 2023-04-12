from django.shortcuts import render, redirect
# from mysql.connector import cursor
import pymysql
from django.views.decorators.http import require_http_methods


class BoardClass:
    def __init__(self, bno, title, content, writer, regDate, updateDate):
        self.bno = bno
        self.title = title
        self.content = content
        self.writer = writer
        self.regDate = regDate
        self.updateDate = updateDate


# Create your views here.
def board(request):
    # return render(request, "board/board.html")
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='tilburg_club', charset='utf8')
    cur = conn.cursor()
    sql_select = "select bno, title, content, writer, DATE_FORMAT(regDate, '%Y%m%d%H%i%s'), DATE_FORMAT(updateDate, '%Y%m%d%H%i%s') from TBL_BOARD"  # where borad = (%s) and 한페이지?
    cur.execute(sql_select)
    rows = cur.fetchall()
    list1 = []
    for row in rows:
        boardClass = BoardClass(row[0],row[1],row[2],row[3],row[4],row[5])
        list1.append(boardClass)
    # request.session['list'] = list1
    print(rows)
    context = {'board_list': list1}
    return render(request, 'board/list.html', context)

def register(request):
    print("---------POST 2 --------")
    return render(request, 'board/register.html')



@require_http_methods(['GET'])
def register_get(request):
    print("---------GET 1 --------")
    return render(request, 'board/register.html')

@require_http_methods(['POST'])
def register_post(request):
    print("---------POST 2 --------")
    return render(request, 'board/register.html')


def board_write(request):
    # return render(request, "board/board_write.html")

    return render(request, "board/register.html")

def board_list(request):
    return


    # conn = pymysql.connect(host='130.162.154.239', user='dev', password='1234', db='tilburg_club', charset='utf8')
    # cur = conn.cursor()
    # sql_select = "select * from board" #where borad = (%s) and 한페이지?
    # cur.execute(sql_select)

    # INSERT INTO TBL_BOARD(TITLE, CONTENT, WRITER) VALUES('테스트 제목5', '테스트 내용', 'user00');

    # for row in cur.fetchall():
    #     print(row)
    #
    # conn.close()

