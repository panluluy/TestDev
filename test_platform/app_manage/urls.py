from django.urls import path
from app_manage.views import project
from app_manage.views import module

urlpatterns = [
    # 项目管理
    path('manage',project.manage),
    # 项目创建
    path('add',project.add_project),
    path('edit/<int:pid>/',project.edit_project),
    path('delete/<int:pid>/',project.delete_project),
    # 模块管理
    path('module_manage/',module.list_module),
]