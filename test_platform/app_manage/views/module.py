from django.shortcuts import render
from django.http import HttpResponseRedirect
from app_manage.models import Module
from app_manage.forms import ModuleForm,ModuleEditForm

def list_module(request):
    """模块管理"""
    module_list = Module.objects.all()
    return render(request,'module/list.html',{"modules":module_list})

def add_module(request):
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            project = form.cleaned_data['project']
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            Module.objects.create(project=project,name=name,describe=describe)
        return HttpResponseRedirect('/manage/module_list/')
    else:
        form = ModuleForm()
    return render(request, 'module/add.html/',{'form':form})

def edit_module(request,pid):
    print('pid:',pid)
    if request.method == 'POST':
        form = ModuleEditForm(request.POST)
        if form.is_valid():
            project = form.cleaned_data['project']
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            m = Module.objects.get(id=pid)
            m.project = project
            m.name = name
            m.describe = describe
            m.save()
        return HttpResponseRedirect('/manage/module_list/')
    else:
        if pid:
            m = Module.objects.get(id=pid)
            form = ModuleForm(instance=m)
        else:
            form = ModuleForm()
        return render(request,'module/edit.html',{'form':form,'id':pid})

def delete_module(request,pid):
    if request.method == 'GET':
        m = Module.objects.get(id=pid)
        m.delete()
        return HttpResponseRedirect('/manage/module_list/')
    else:
        return HttpResponseRedirect('/manage/module_list/')