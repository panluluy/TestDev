from django.urls import path
from app_manage.views import project
from app_manage.views import module

urlpatterns = [
    # 项目管理
    path('',project.manage),
    path('project_list/',project.manage),
    path('project_add/',project.add_project),
    path('project_edit/<int:pid>/',project.edit_project),
    path('project_delete/<int:pid>/',project.delete_project),
    # 模块管理
    path('module_list/',module.list_module),
    path('module_add/',module.add_module),
    path('module_edit/<int:pid>/',module.edit_module),
    path('module_delete/<int:pid>/',module.delete_module),
]