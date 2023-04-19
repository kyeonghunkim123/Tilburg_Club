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
    # path("h_modify", boardapp.h_modify, name="modify"),
    # path("h_remove", boardapp.h_remove, name="remove"),
    # path("getAttachList", boardapp.h_remove, name="remove"),

    # -- 2023.04.12. KKH 추가 끝 --

    # -- 2023.04.13. KKH 테스트 시작 --
    path('abracadabra0', boardapp.h_list_ver2, name="h_list_ver2"),
    path('abracadabra1', boardapp.banana1, name="banana1"),
    # -- 2023.04.12. KKH 테스트 끝 --
]
