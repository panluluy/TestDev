from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(requests):
    return render(requests,'hello.html')

"""
django的处理过程：
1.url指定路径:/hello
2.setting.py 找到url的配置文件
3.urls.py匹配路径/hello，把请求指到views文件
4.在views.py写入Response处理，把templates目录下的html文件返回给客户端
"""

