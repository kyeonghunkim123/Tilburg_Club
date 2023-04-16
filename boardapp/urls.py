from django.urls import path
import boardapp.views as boardapp

urlpatterns = [
    path("board", boardapp.board, name="board"),
    path("board_write", boardapp.board_write, name="write"),
    path("board_list", boardapp.board_list, name="blist"),

    # -- 2023.04.12. KKH 추가 시작 --
    path("h_list", boardapp.h_list, name="list"),
    path("h_register_get", boardapp.h_register_get, name="register"),
    path("h_register_post", boardapp.h_register_post),
    path("h_modify", boardapp.h_modify, name="modify"),
    # -- 2023.04.12. KKH 추가 끝 --
    # path("board_main", boardapp, name='board_main')

]

# urlpatterns = [
#     path("login", userapp.login)
#     ]