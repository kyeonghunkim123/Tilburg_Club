from django.urls import path
import boardapp.views as boardapp

urlpatterns = [
    path("board", boardapp.board),
    path("board_write", boardapp.board_write)
    ]

# urlpatterns = [
#     path("login", userapp.login)
#     ]