from django.urls import path
from . import views

print('여기는 startWeb에 urls.py 파일')
urlpatterns = [
    path('', views.index, name='index'),
    path('join', views.join, name='join'),
    path('login', views.login, name='login'),
    path('loginSubmit', views.loginSubmit, name='loginSubmit'),
]