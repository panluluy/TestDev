from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app_manage.models import Project

# Create your views here.
@login_required
def manage(request):
    project_list = Project.objects.all()
    return render(request,'manager.html',{'projects':project_list})
