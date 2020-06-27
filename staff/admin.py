from django.contrib import admin
from . import models
# Register your models here.


class StaffManager(admin.ModelAdmin):
    list_display = ['name', 'state']


admin.site.register(models.Staff, StaffManager)