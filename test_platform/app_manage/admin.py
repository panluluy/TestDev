from django.contrib import admin
from app_manage.models import Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name','describe','status','update_time','create_time']
    search_fields = ['name']
    list_filter = ['status']

admin.site.register(Project,ProjectAdmin)