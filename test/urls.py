"""test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
#     path('start/', include('startWeb.urls')),
#     path('admin/', admin.site.urls),
#
# ]
from django.contrib import admin
from django.urls import path, include
import startWeb.views as starWebviews # 모듈을 사용하듯 import
print('여기는 test에 urls.py 파일')
urlpatterns = [
    path('start/', include('startWeb.urls')),
    path('user/', include('startWeb.urls')),
    # path('경로', views.py에 만들어둔 함수)
    path('', starWebviews.main), # index.html의 역할
    path('hello1/', starWebviews.hello1),
    path('admin/', admin.site.urls), # 기본 path
]


