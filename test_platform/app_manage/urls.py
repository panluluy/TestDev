from django.urls import path
from app_manage.views import project

urlpatterns = [
    # 项目管理
    path('manage',project.manage),  # 跳转至app_manage\views.py文件manage函数
    # 项目创建
    path('add',project.add_project),
    path('edit/<int:pid>/',project.edit_project),
    path('delete/<int:pid>/',project.delete_project),
]