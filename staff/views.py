import json

from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from admins.sessions import verify_permission
from staff import models


def staff(request):
    if request.method == "GET":
        try:
            #查询员工信息
            staffs = models.Staff.objects.filter().order_by('department')
        except:
            return HttpResponse("失败")
        return render(request, "member-list.html",locals())

@verify_permission
def staff_add(request, per_list):
    if per_list['add_staff'] != '0':
        return HttpResponse("权限不足")
    if request.method == 'GET':
        return render(request, "member-add.html")
    if request.method == "POST":
        name = request.POST.get('name')
        department = request.POST.get('department')
        state = request.POST.get('state')
        sex = request.POST.get('sex')
        tel = request.POST.get('tel')
        duty = request.POST.get('duty')
        education = request.POST.get('education')
        card = request.POST.get('card')
        try:
            #创建员工信息
            models.Staff.objects.create(name=name, department=department, state=state, sex=sex, tel=tel, duty=duty, education=education, card=card)
        except:
            return HttpResponse("失败")
        code = 200
        return render(request, "member-add.html", locals())


@verify_permission
def staff_del(request, id, per_list):
    if per_list['add_staff'] != '0':
        return HttpResponse("权限不足")
    if request.method == 'DELETE':
        try:
            staff = models.Staff.objects.get(id=id)
            staff.delete()
        except Exception as e:
            return HttpResponse("删除失败")
        return JsonResponse({'code': 200})

@verify_permission
def staff_edit(request, id, per_list):
    if per_list['add_staff'] != '0':
        return HttpResponse("权限不足")
    if request.method == 'GET':
        try:
            re = models.Staff.objects.get(id=id)
        except Exception as e:
            return HttpResponse("数据错误")
        return render(request, "member-edit.html", locals())

    if request.method == 'POST':

        name = request.POST.get('name')
        department = request.POST.get('department')
        state = request.POST.get('state')
        sex = request.POST.get('sex')
        tel = request.POST.get('tel')
        duty = request.POST.get('duty')
        education = request.POST.get('education')
        card = request.POST.get('card')
        #try:
        res = models.Staff.objects.filter(id=id)
        res.update(name=name, department=department, state=state, sex=sex, tel=tel, duty=duty, education=education, card=card)
        #except Exception as e:
        #    return HttpResponse("删除失败")
        code = 200
        return render(request, "member-edit.html", locals())


def sreach(request, content):
    if request.method == 'GET':
        staffs = models.Staff.objects.filter(name=content)
        if not staffs:
            staffs = models.Staff.objects.filter(department=content)
        return render(request, "member-sreach.html",locals())



