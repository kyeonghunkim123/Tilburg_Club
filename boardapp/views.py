from django.shortcuts import render, redirect
import pymysql

# Create your views here.
def board(request):
    return render(request, "board/board.html")

def board_write(request):
    return render(request, "board/board_write.html")
def board_list(request):
    filename = "C:/tilburg_club/tilburg.txt"
    with open(filename) as f:
        root_ps = f.read()
    dev_ps = root_ps + 'dev'

    conn = pymysql.connect(host='130.162.154.239', user='dev', password=dev_ps, db='tilburg_club', charset='utf8')
    cur = conn.cursor()
            # 쿼리 실행
            sql = 'SELECT * FROM board_table'
            cur.execute(sql)

            # 결과 출력
            result = cursor.fetchall()
            for row in result:
                print(row)

    finally:
        # 연결 종료
        conn.close()
