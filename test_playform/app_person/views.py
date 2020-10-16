from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def hello(requests):
    return render(requests,'hello.html')

def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    if request.method=="POST":
        username = request.POST.get("username",'')
        password = request.POST.get('password','')
        if username=="" or password=="":
            return render(request,"login.html",{"error":"用户名或者密码为空"})
        user = auth.authenticate(username=username,password=password)
        print("用户是否存在",user)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect("/project")
        else:
            return render(request,'login.html',{"error":"用户名或者密码错误"})


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

"""
django的处理过程：
1.url指定路径:/hello
2.setting.py 找到url的配置文件
3.urls.py匹配路径/hello，把请求指到views文件
4.在views.py写入Response处理，把templates目录下的html文件返回给客户端
"""

