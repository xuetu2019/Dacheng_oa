from django.db import models

# Create your models here.
from admins.models import Admins


class Process(models.Model):
    process = models.CharField(max_length=50, verbose_name='流程')
    content = models.TextField(max_length=50, verbose_name='内容')
    file = models.ImageField(upload_to='file_process/', null=True)
    ceo_check = models.CharField(max_length=20, null=True)
    cto_check = models.CharField(max_length=20, null=True)
    ceo_content = models.TextField(max_length=50, null=True)
    cto_content = models.TextField(max_length=50, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    cate = models.CharField(max_length=50, null=True, verbose_name='部门')
    admin = models.ForeignKey(Admins, null=True)

    class Meta:
        db_table = 'process'