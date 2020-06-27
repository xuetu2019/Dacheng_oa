from django.db import models

# Create your models here.


class Cars(models.Model):
    car = models.CharField(max_length=15, verbose_name='车牌') #varchar(30),加索引
    department = models.CharField(max_length=30, verbose_name='线路')
    state = models.CharField(max_length=15, verbose_name='状态')
    age = models.IntegerField(verbose_name='车龄')
    buy_time = models.DateField(verbose_name='购买日期')
    logo = models.CharField(max_length=30, verbose_name='品牌')
    sites = models.IntegerField(verbose_name='座位')
    check = models.DateField(verbose_name='检车日期')

    class Meta:
        db_table = 'cars'