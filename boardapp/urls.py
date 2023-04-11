from django.urls import path
import boardapp.views as boardapp

urlpatterns = [
    path("board", boardapp.board),
    path("board_write", boardapp.board_write),
    path('register', boardapp.register, name="register"),
    ]

# urlpatterns = [
#     path("login", userapp.login)
#     ]


