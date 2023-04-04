from django.urls import path

import userapp.views as userapp

urlpatterns = [
    path("mainpage", userapp.mainpage),
    path("login", userapp.login),
    path("join_membership", userapp.join),
    path("logout", userapp.logout),
    path("find_pw", userapp.find_pw),
    path("find_mp", userapp.find_mp)
    ]

# urlpatterns = [
#     path("login", userapp.login)
#     ]