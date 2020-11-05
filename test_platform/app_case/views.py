from django.shortcuts import render
from django.http import JsonResponse

def list_case(request):
    """用例管理"""
    return render(request,'case/debug.html',)

def send_req(request):
    if request.method=='GET':
        id = request.GET.get("id")
        name = request.GET.get("name")
    return JsonResponse({"status":200,"msg":"success"})
