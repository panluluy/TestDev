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
    if request.method == 'GET':
        url = request.GET.get("url", '')
        method = request.GET.get("method", '')
        header = request.GET.get("header", '')
        par_type = request.GET.get("par_type", '')
        par_value = request.GET.get("par_value", '')

        print('header', header, type(header))
        print("url", url, type(url))
        print("method", method, type(method))

        # 后端增加对url进行校验
        if url == "":
            return JsonResponse({"status": 10101, "message": "URL参数不能为空"})
        if header == "":
            pass
        else:
            try:
                header = json.loads(header)
            except json.decoder.JSONDecodeError:
                return JsonResponse({"status": 10102, "message": "请求头参数填写有误"})

        if method == "get":
            r = requests.get(url, params=par_value, headers=header)

        if method == 'post':
            if par_type == "form":
                r = requests.post(url, data=par_value, headers=header)
            if par_type == "json":
                # 增加对json数据类型时，请求头不能为空的判断
                if header == "":
                    return JsonResponse({"status": 10101, "message": "请求头不能为空"})
                try:
                    par_value = json.loads(par_value)
                except json.decoder.JSONDecodeError:
                    return JsonResponse({"status": 10102, "message": "json参数必须使用双引号"})
                print("par_value", par_value, type(par_value))
                r = requests.post(url, json=par_value, headers=header)

    return JsonResponse({"status": 200, "msg": "success", "data": r.text})

def assert_result(request):
    """
    断言结果
    """
    print(request.method)
    if request.method == "GET":
        result_text = request.GET.get("result_text", "")
        assert_text = request.GET.get("assert_text", "")
        assert_type = request.GET.get("assert_type", "")
        # print(result_text)
        # print(assert_text)
        # print(assert_type)

        if result_text == "" or assert_text == "":
            return JsonResponse({"code": 10101, "message": "断言的参数不能为空"})

        if assert_type != "include" and assert_type != "equal":
            return JsonResponse({"code": 10102, "message": "断言的类型错误"})

        if assert_type == "include":
            if assert_text in result_text:
                return JsonResponse({"code": 10200, "message": "断言包含成功"})
            else:
                return JsonResponse({"code": 10200, "message": "断言包含失败"})

        if assert_type == "equal":
            if assert_text == result_text:
                return JsonResponse({"code": 200, "message": "断言相等成功"})
            else:
                return JsonResponse({"code": 200, "message": "断言相等失败"})

        return JsonResponse({"code": 10102, "message": "fail"})
    else:
        return JsonResponse({"code": 10100, "message": "请求方法错误"})