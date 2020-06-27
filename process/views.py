from time import time

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from admins.sessions import verify_permission
from process import models

@verify_permission
def show_self_process(request, per_list):
    admin = request.session['username']
    if per_list['check_office'] == '0' and per_list['check_operation'] == '0' and per_list['check_staff'] == '0':
        # 权限类别
        cate = 'check_all'
    elif per_list['check_operation'] == '0':
        cate = 'check_operation'
    elif per_list['check_staff'] == '0':
        cate = 'check_staff'
    elif per_list['check_office'] == '0':
        cate = 'check_office'
    else:
        cate = None
        process = models.Process.objects.filter(admin_id=admin)
    if cate:
        process = models.Process.objects.all()
    return render(request,"process_show.html", locals())

@verify_permission
def add_process(request, per_list):
    if per_list['sta_office'] == '0':
        #权限类别
        cate = 'sta_office'
    elif per_list['sta_opration'] == '0':
        cate = 'sta_opration'
    elif per_list['sta_staff'] == '0':
        cate = 'sta_staff'
    else:
        return HttpResponse("权限不足")
    if request.method == 'POST':
        re = request.session['username']
        process_name = request.POST.get('process_name','')
        process_content = request.POST.get('process_content', '')
        file = request.FILES.get("myfile", None)
        try:
            models.Process.objects.create(process=process_name, content=process_content, file=file, cate=cate, admin_id=re)
            code =200
        except:
            return JsonResponse({'code': 800, 'error': '上传失败'})
        return render(request, "add_process.html", locals())

    return render(request,"add_process.html")

@verify_permission
def process_check(request, id, per_list):
    if request.method == 'POST':
        if per_list['check_office'] == '0' and per_list['check_operation'] == '0' and per_list['check_staff'] == '0':
            # 权限类别
            cate = 'check_all'
        elif per_list['check_operation'] == '0':
            cate = 'check_operation'
        elif per_list['check_staff'] == '0':
            cate = 'check_staff'
        elif per_list['check_office'] == '0':
            cate = 'check_office'
        else:
            return HttpResponse("权限不足")
    #流程同意时发来的data
    check = request.POST.get('data')
    role = request.GET.get('role')
    #res是流程的实体
    res = models.Process.objects.get(id=id)
    if role == 'CTO':
        res.cto_check = check
        res.save()
    if role == 'CEO' and cate == 'check_all':
        res.ceo_check = check
        res.save()
    #查看流程详情
    if request.method == 'GET':
        res = models.Process.objects.get(id=id)
        return render(request, "process_check.html", locals())
    return JsonResponse({'code': 200})

def del_process(request):
    pass