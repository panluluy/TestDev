from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app_manage.models import Project

# Create your views here.
@login_required
def manage(request):
    project_list = Project.objects.all()
    return render(request,'project_list.html',{'projects':project_list})

def add_project(request):
    return render(request, 'add_project.html')