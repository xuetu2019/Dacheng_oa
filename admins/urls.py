from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.show_admins),
    url(r'^add_admin', views.add_admin),
    url(r'^del_admin/(\w+)', views.del_admin),
    # url(r'^edit/(\d+)', views.staff_edit),
    # url(r'^sreach/(\w+)', views.sreach),
]