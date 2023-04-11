from django.urls import path
import boardapp.views as boardapp

urlpatterns = [
    path("board", boardapp.board),
    path("board_write", boardapp.board_write),
    path("board_reg",boardapp.board_reg)
    ]

# urlpatterns = [
#     path("login", userapp.login)
#     ]