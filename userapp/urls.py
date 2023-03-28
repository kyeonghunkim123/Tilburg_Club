from django.urls import path

import userapp.views as userapp

urlpatterns = [
    path("mainpage", userapp.mainpage)
    ]