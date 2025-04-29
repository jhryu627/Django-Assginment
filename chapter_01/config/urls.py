"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# urls.py
# urls.py
from django.contrib import admin
from django.http import Http404
from django.shortcuts import render
from django.urls import path
from fake_db import user_db  # fake_db에서 user_db를 import

_db = user_db

# 홈 페이지 뷰 정의
def home(request):
    return render(request, 'home.html')

def user_list(request):
    names = [{'id': key, 'name': value['이름']} for key, value in _db.items()]
    return render(request, 'user_list.html', {'data': names})

def user_info(request, user_id):
    if user_id not in _db:
        raise Http404('User not found')
    info = _db[user_id]
    return render(request, 'user_info.html', {'data': info})

urlpatterns = [
    path('', home, name='home'),  # 루트 경로에 대한 URL 패턴 추가
    path('users/', user_list, name='user_list'),
    path('users/<int:user_id>/', user_info, name='user_info'),
    path('admin/', admin.site.urls),
]

