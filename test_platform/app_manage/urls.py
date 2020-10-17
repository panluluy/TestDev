from django.urls import path
from app_manage import views

urlpatterns = [
    # 项目管理
    path('',views.manage),  # 跳转至app_manage\views.py文件manage函数
    # 项目创建
    path('add',views.add_project)
]