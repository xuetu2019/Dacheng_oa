from django.db import models


class Staff(models.Model):
    name = models.CharField(max_length=15, verbose_name='姓名') #varchar(30),加索引
    department = models.CharField(max_length=30, verbose_name='部门')
    state = models.CharField(max_length=15, verbose_name='状态')
    sex = models.CharField(max_length=3, verbose_name='性别')
    tel = models.CharField(max_length=15, unique=True, verbose_name='电话')
    duty = models.CharField(max_length=30, verbose_name='职位')
    education = models.CharField(max_length=15, verbose_name='学历')
    card = models.CharField(max_length=20, db_index=True, unique=True, verbose_name='身份证')

    def __str__(self):
        return "姓名：" + self.name

    class Meta:
        db_table = 'staff'


    
