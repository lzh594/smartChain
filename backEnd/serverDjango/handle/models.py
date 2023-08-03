from django.db import models


# Create your models here.
# 用户提交信息数据库
class UsrData(models.Model):
    HashID = models.CharField(max_length=45, verbose_name="哈希索引", name="HashID")
    Phone = models.CharField(max_length=11, verbose_name="手机号", name="Phone")
    Superior = models.CharField(max_length=10, verbose_name="应用商", name="Superior")
    App = models.CharField(max_length=10, verbose_name="所选app", name="App")
    Op = models.CharField(max_length=10, verbose_name="操作", name="Op")
    State = models.CharField(max_length=10, verbose_name="当前状态", name="State")
    TimeStamp = models.CharField(max_length=25, verbose_name="时间戳", name="TimeStamp")


# 历史记录数据库
class History(models.Model):
    Phone = models.CharField(max_length=11, verbose_name="手机号", name="Phone")
    Superior = models.CharField(max_length=10, verbose_name="应用商", name="Superior")
    App = models.CharField(max_length=10, verbose_name="所选app", name="App")
    Op = models.CharField(max_length=10, verbose_name="操作", name="Op")
    TimeStamp = models.CharField(max_length=25, verbose_name="时间戳", name="TimeStamp")
