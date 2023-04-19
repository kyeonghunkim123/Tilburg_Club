from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
# from mysql.connector import cursor
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








# -- 2023.04.12. KKH 추가 시작 --

class BoardClass:
    def __init__(self, bno, title, content, writer, regDate, updateDate):
        self.bno = bno
        self.title = title
        self.content = content
        self.writer = writer
        self.regDate = regDate
        self.updateDate = updateDate


def add_all (*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum



def h_list(request):
    filename = "C:/tilburg_club/tilburg.txt"
    with open(filename) as f:
        root_ps = f.read().strip()
    dev_ps = root_ps + 'dev'
    print(dev_ps)

    conn = pymysql.connect(host='130.162.154.239', user='dev', password=dev_ps, db='tilburg_club', charset='utf8')
    # conn = pymysql.connect(host='localhost', user='root', password='1234', db='tilburg_club', charset='utf8')
    cur = conn.cursor()
    sql_select = "select bno, title, content, writer, DATE_FORMAT(regDate, '%Y%m%d%H%i%s'), DATE_FORMAT(updateDate, '%Y%m%d%H%i%s') from TBL_BOARD ORDER BY bno desc LIMIT 10 OFFSET 0"
    # cur.execute(sql_select)
    temp_result = cur.execute(sql_select)
    rows = cur.fetchall()
    list1 = []
    print("\n\n\n\n\n===========================")
    print("temp_result : ", temp_result)
    print("type(rows): ", type(rows))
    print("------------------------------")
    print("rows : ", rows)
    print("------------------------------")
    print("===========================\n\n\n\n\n")
    for row in rows:
        boardClass = BoardClass(row[0],row[1],row[2],row[3],row[4],row[5])
        list1.append(boardClass)
    context = {'board_list': list1}
    return render(request, 'board/h_list.html', context)

def h_list_ver2(request):
    filename = "C:/tilburg_club/tilburg.txt"
    with open(filename) as f:
        root_ps = f.read().strip()
    dev_ps = root_ps + 'dev'
    print(dev_ps)

    conn = pymysql.connect(host='130.162.154.239', user='dev', password=dev_ps, db='tilburg_club', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()
    sql_select = "select bno, title, content, writer, DATE_FORMAT(regDate, '%Y%m%d%H%i%s') as regDate, DATE_FORMAT(updateDate, '%Y%m%d%H%i%s') as updateDate from TBL_BOARD ORDER BY bno desc LIMIT 10 OFFSET 0"
    temp_result = cur.execute(sql_select)
    rows = cur.fetchall()
    list1 = []
    print("\n\n\n\n\n===========================")
    print(f"temp_result : {temp_result}, type(temp_result) : {type(temp_result)}, type(str(temp_result)) : {type(str(temp_result))}")
    print("type(rows): ", type(rows))
    print("------------------------------")
    print("rows : ", rows)
    print("------------------------------")
    print("===========================\n\n\n\n\n")

    for row in rows:
        boardClass = BoardClass(**row) # // 의미
        print(row['bno'])
        # boardClass = BoardClass(bno= 13, title= '테스트 제목1', content= '테스트 내용1', writer= 'user01', regDate= '20230412152817', updateDate= '20230412152817')
        # boardClass = BoardClass(13, '테스트 제목1', '테스트 내용1', 'user01', '20230412152817',  '20230412152817')
        list1.append(boardClass)
    context = {'board_list': list1}


    # c = add_all()
    print("-------------")
    # temp =
    print(     add_all((1, 2, 3, 4, 5))     )
    print("-------------")
    return render(request, 'board/h_list.html', context)





@require_http_methods(['GET'])
def h_register_get(request):
    print("---------GET 1 --------")
    return render(request, 'board/h_register.html')

@require_http_methods(['POST'])
def h_register_post(request):
    print("---------POST 2 --------")
    # 아래 수정해야함.
    return render(request, 'board/h_register.html')


def h_modify(request):
    return render(request, 'board/h_modify.html')

    # -- 2023.04.12. KKH 추가 끝 --




# --------------------------------------




def banana1(request):
    class Product():
        def __init__(self, name, price):
            self.name = name
            self.price = price

        def print1(self):
            print(f'{self.name}의 가격은 {self.price} 입니다.')

    apple = Product('사과', 1500)
    grape = Product('포도', 3000)
    fruits = [apple, grape]
    for fruit in fruits:
        fruit.print1()


    class Fruit(Product):
        def __init__(self, name, price, color):
            super().__init__(name, price)
            # ERROR # super().name = name ; super().price = price
            self.color = color

        def print1(self):
            super().print1()
            print(f'색깔은 {self.color}입니다.')

        def return1(self):
            return f'색깔은 {self.color}입니다.'


    banana = Fruit('바나나', 2000, '노란색')
    banana.print1()

    temp = banana.return1()
    str = "<h1>" +  temp  + "</h1>"
    return HttpResponse(str)

# ---------------------------------



