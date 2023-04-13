from django.urls import path
import boardapp.views as boardapp

urlpatterns = [
    path("board", boardapp.board),
    path("board_write", boardapp.board_write),
    path("board_list", boardapp.board_list),

    # -- 2023.04.12. KKH 추가 시작 --
    path("h_list", boardapp.h_list, name="list"),
    path("h_register_get", boardapp.h_register_get, name="register"),
    path("h_register_post", boardapp.h_register_post),
    path("h_modify", boardapp.h_modify, name="modify"),
    # -- 2023.04.12. KKH 추가 끝 --

]

# urlpatterns = [
#     path("login", userapp.login)
#     ]