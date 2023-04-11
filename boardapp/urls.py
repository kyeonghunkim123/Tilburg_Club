from django.urls import path
import boardapp.views as boardapp

urlpatterns = [
    path("board", boardapp.board),
    path("board_write", boardapp.board_write),
    path("board_list", boardapp.board_list)
    ]

# urlpatterns = [
#     path("login", userapp.login)
#     ]