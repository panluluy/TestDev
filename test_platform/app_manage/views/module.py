from django.shortcuts import render
from django.http import HttpResponseRedirect
from app_manage.models import Module
from app_manage.forms import ModuleForm

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
        return HttpResponseRedirect('/manage/')
    else:
        form = ModuleForm()
    return render(request, 'module/add.html',{'form':form})