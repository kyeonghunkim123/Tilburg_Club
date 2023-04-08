from django.urls import path

import board.views as board
import userapp.views as userapp

urlpatterns = [
    path("mainpage", userapp.mainpage),
    path("login", userapp.login),
    path("join_membership", userapp.join),
    path("logout", userapp.logout),
    path("find_pw", userapp.find_pw),
    path("find_mp", userapp.find_mp),
    path("find_id", userapp.find_id),
    path("find_mi", userapp.find_mi),
    path("complete_join", userapp.complete_join),
    path("board", board.board),
    path("complete_login", userapp.complete_login),
    path("board_write", board.board_write)
    ]

# urlpatterns = [
#     path("login", userapp.login)
#     ]