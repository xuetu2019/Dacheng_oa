from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.show_self_process),
    url(r'^add_process', views.add_process),
    url(r'^del_process/(\w+)', views.del_process),
    url(r'^process_check/(\d+)', views.process_check),
    # url(r'^edit/(\d+)', views.staff_edit),
    # url(r'^sreach/(\w+)', views.sreach),
]