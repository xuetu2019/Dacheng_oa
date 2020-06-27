from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from admins import models
from admins.sessions import verify_permission


def show_admins(request):

    try:
        # 查询admin
        admins = models.Admins.objects.all()
    except:
        return HttpResponse("失败")
    admins_list = []
    for admin in admins:
        username = admin.username
        permissions = admin.permission_set.all()

        per_list = []
        for per in permissions:
            per_list = [per.add_admin, per.add_staff, per.up_file, per.show_file, per.check_staff, per.check_operation,\
                        per.check_office, per.sta_staff, per.sta_opration, per.sta_office]
            per_list.append(per)
        user = {'name':username,'per':per_list}
        admins_list.append(user)

    return render(request, "admin-list.html", locals())

@verify_permission
def add_admin(request, per_list):
    if per_list['add_admin'] != '0':
        return HttpResponse("权限不足")
    if request.method == 'GET':

        return render(request, "admin-add.html")
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pass')
        add_admin = request.POST.get('add_admin')
        add_staff = request.POST.get('add_staff')
        up_file = request.POST.get('up_file')
        show_file = request.POST.get('show_file')
        check_staff = request.POST.get('check_staff')
        check_operation = request.POST.get('check_operation')
        check_office = request.POST.get('check_office')
        sta_staff = request.POST.get('sta_staff')
        sta_opration = request.POST.get('sta_opration')
        sta_office = request.POST.get('sta_office')
        print(add_admin)
        try:
            # 创建admin信息
            models.Admins.objects.create(username=username, pwd=pwd)
        except:
            return HttpResponse("admins失败")
        try:
            # 创建permission信息
            models.Permission.objects.create(add_admin=add_admin, add_staff=add_staff,up_file=up_file, show_file=show_file, check_staff=check_staff, check_operation=check_operation,check_office=check_office, sta_staff=sta_staff, sta_opration=sta_opration, sta_office=sta_office, admin_id=username)
        except:
            return HttpResponse("permission失败")

        return JsonResponse({'code': 200})

@verify_permission
def del_admin(request, admin, per_list):
    if per_list['add_admin'] != '0':
        return HttpResponse("权限不足")
    if request.method == 'DELETE':
        try:
            per = models.Permission.objects.get(admin_id=admin)
            per.delete()
        except:
            return HttpResponse("per失败")
        try:
            admin_del = models.Admins.objects.get(username=admin)
            admin_del.delete()
        except:
            return HttpResponse("admin失败")
    return JsonResponse({'code': 200})