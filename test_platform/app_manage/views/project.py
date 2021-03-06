from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from app_manage.models import Project
from app_manage.forms import ProjectForm,ProjectEditForm

# Create your views here.
@login_required
def manage(request):
    # 获取登录成功后返回的cookie
    username = request.COOKIES.get('user')
    project_list = Project.objects.all()
    # 返回用户名
    return render(request,'project/list.html',{'projects':project_list,'user':username})

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            status = form.cleaned_data['status']
            Project.objects.create(name=name,describe=describe,status=status)
        return HttpResponseRedirect('/manage/')
    else:
        form = ProjectForm()
    return render(request, 'project/add.html',{'form':form})

def edit_project(request,pid):
    print('pid:',pid)
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            status = form.cleaned_data['status']
            p = Project.objects.get(id=pid)
            p.name = name
            p.describe = describe
            p.status = status
            p.save()
        return HttpResponseRedirect('/manage/')
    else:
        if pid:
            p = Project.objects.get(id=pid)
            print(p.name)
            form = ProjectEditForm(instance=p)
        else:
            form = ProjectForm()
        return render(request,'project/edit.html',{'form':form,'id':pid})

def delete_project(request,pid):
    if request.method == 'GET':
        p = Project.objects.get(id=pid)
        p.delete()
        return HttpResponseRedirect('/manage/')
    else:
        return HttpResponseRedirect('/manage/')