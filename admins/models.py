from django.db import models

# Create your models here.


class Admins(models.Model):
    username = models.CharField(max_length=15, primary_key=True, verbose_name='姓名') #varchar(30),加索引
    pwd = models.CharField(max_length=32)

    def __str__(self):
        return "姓名：" + self.username

    class Meta:
        db_table = 'admins'


class Permission(models.Model):
    add_admin = models.CharField(max_length=2, null=True)
    add_staff= models.CharField(max_length=2,null=True)
    up_file= models.CharField(max_length=2,null=True)
    show_file= models.CharField(max_length=2,null=True)
    check_staff= models.CharField(max_length=2,null=True)
    check_operation= models.CharField(max_length=2,null=True)
    check_office= models.CharField(max_length=2,null=True)
    sta_staff= models.CharField(max_length=2,null=True)
    sta_opration= models.CharField(max_length=2,null=True)
    sta_office= models.CharField(max_length=2,null=True)
    admin = models.ForeignKey(Admins, null=True)


    class Meta:
        db_table = 'permission'