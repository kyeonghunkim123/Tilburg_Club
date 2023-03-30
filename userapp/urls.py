from django.urls import path

import userapp.views as userapp

urlpatterns = [
    path("mainpage", userapp.mainpage),
    path("login", userapp.login),
    path("join_membership", userapp.join),
    path("logout", userapp.logout)
    ]

# urlpatterns = [
#     path("login", userapp.login)
#     ]