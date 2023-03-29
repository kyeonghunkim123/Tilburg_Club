from django.urls import path

import userapp.views as userapp

urlpatterns = [
    path("mainpage", userapp.mainpage),
    path("login", userapp.login),
    path("logout", userapp.logout)
    ]

# urlpatterns = [
#     path("login", userapp.login)
#     ]