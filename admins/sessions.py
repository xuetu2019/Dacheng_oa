from django.http import HttpResponse

from admins import models

list = ['add_admin', 'add_staff', 'up_file', 'show_file', 'check_staff', 'check_operation', 'check_office', 'sta_staff',\
        'sta_office', 'sta_opration']
def verify_permission(func):
    def wrapper(request, *arg, **kwargs):
        re = request.session['username']
        if re:
            try:
                admin = models.Admins.objects.get(username=re)
            except:
                return HttpResponse('admin_error')
            try:
                permission = models.Permission.objects.get(admin_id=admin.username)
                per_list = {}
                for per in dir(permission):
                    if per in list:
                        re = getattr(permission,per)
                        per_list[per] = re
            except:
                return HttpResponse('per_error')

            return func(request, *arg,per_list,  **kwargs)
    return wrapper
