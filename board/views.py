from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import pymysql

# Create your views here.
def board(request):
    return render(request,  "board/board.html")
def board_write(request):
    return render(request,  "board/board_write.html")
