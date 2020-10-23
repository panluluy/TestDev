from django.contrib import admin
from app_manage.models import Project
from app_manage.models import Module

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name','describe','status','update_time','create_time']
    search_fields = ['name']
    list_filter = ['status']
admin.site.register(Project,ProjectAdmin)

class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name','describe','create_time','project']
admin.site.register(Module,ModuleAdmin)