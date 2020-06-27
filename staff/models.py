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


    #def __str__(self):
        #return self.title #后台管理时显示书名


# class Athur(models.Model):
#     name = models.CharField(max_length=30) #varchar(30),加索引
#     age = models.IntegerField(null=True)
#     email = models.EmailField(null=True)
#
#     def __str__(self):
#         return self.name #后台管理时显示书名
#     #2，厉害的方法ModelAdin
#
#
# class Wife(models.Model):#想要在管理页面出现，还要去admin.py中设置
#     name = models.CharField(max_length=30) #varchar(30)
#     author = models.OneToOneField(Athur)#数据表李会有author_id字段且唯一