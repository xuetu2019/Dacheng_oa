from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.staff),
    url(r'^add', views.staff_add),
    url(r'^del/(\d+)', views.staff_del),
    url(r'^edit/(\d+)', views.staff_edit),
    url(r'^sreach/(\w+)', views.sreach),
]