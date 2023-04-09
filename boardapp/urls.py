from django.urls import path
import boardapp.views as boardapp

urlpatterns = [
    path("board", boardapp.board),
    path("board_write", boardapp.board_write),
    path("board_list", boardapp.board_list),
    path("board_portfolio", boardapp.board_portfolio)
    ]

# urlpatterns = [
#     path("login", userapp.login)
#