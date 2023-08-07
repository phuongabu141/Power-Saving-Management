"""QuanLySTK URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from . import views

app_name = 'normal_site'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('profile/', views.profile, name='profile'),
    path('lap_phieu_tiet_kiem/', views.LapPhieuTietKiem.as_view(), name='lap_phieu_tiet_kiem'),
    path('tim_kiem_phieu_tiet_kiem/', views.TimKiemPhieuTietKiem.as_view(), name='tim_kiem_phieu_tiet_kiem'),
    path('rut_phieu_tiet_kiem/<str:maptk>', views.RutPhieuTietKiem.as_view(), name='rut_phieu_tiet_kiem'),
    #path('tra_cuu/',views.TraCuu.as_view(), name='tra_cuu'),
    path('tra_cuu_2/',views.tracuu, name='tra_cuu'),
    path('thong_ke/',views.ThongKe,name='thong_ke'),
    path('logout/', views.logout, name='logout')
    ]
