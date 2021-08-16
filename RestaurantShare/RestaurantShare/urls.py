"""RestaurantShare URL Configuration
프로젝트 전체를 보여주는 url

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('shareRes.urls')),#https://127.0.0.1:8000/으로 시작되고 따로 아래에 표시되지 않는 요청 처리
    path('sendEmail/',include('sendEmail/urls')),#https://127.0.0.1:8000/sendEmail로 시작되는 요청 처리
    path('admin/', admin.site.urls),
]
