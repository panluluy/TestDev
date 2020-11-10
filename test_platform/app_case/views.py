from django.shortcuts import render
from django.http import JsonResponse
import requests,json

def list_case(request):
    """用例管理"""
    return render(request,'case/debug.html',)

def send_req(request):
    """
    发送接口
    """
    if request.method=='GET':
        url = request.GET.get("url")
        method = request.GET.get("method")
        header = request.GET.get("header")
        par_type = request.GET.get("par_type")
        par_value = request.GET.get("par_value")

        try:
            header = json.loads(header)
        except json.decoder.JSONDecodeError:
            return JsonResponse({"status":400,"message":"请求头参数填写有误"})
        # print('header',header,type(header))
        # print("url",url,type(url))
        # print("method", method, type(method))
        try:
            par_value = json.loads(par_value)
        except json.decoder.JSONDecodeError:
            return JsonResponse({"status":400,"message":"json参数必须使用双引号"})
        print("par_value",par_value,type(par_value))

        if method == "get":
            r = requests.get(url,params=par_value,headers=header)

        if method == 'post':
            if par_type == "form":
                r = requests.post(url,data=par_value,headers=header)
            if par_type == "json":
                r = requests.post(url,json=par_value,headers=header)

    return JsonResponse({"status":200,"msg":"success","data":r.text})
