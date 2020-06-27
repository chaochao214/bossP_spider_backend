from django.db import models


# Create your models here.
class Lagou(models.Model):
    id = models.IntegerField(primary_key=True)
    company = models.CharField(max_length=256)  # 公司
    job = models.CharField(max_length=256)  # 工作
    city = models.CharField(max_length=256)  # 城市
    site = models.CharField(max_length=256)  # 站点
    salary = models.CharField(max_length=256)  # 雇佣
    url = models.CharField(max_length=256)  # 链接

    class Meta:
        db_table = 'lagou'


class Zhipin(models.Model):
    id = models.IntegerField(primary_key=True)
    company = models.CharField(max_length=256)  # 公司
    job = models.CharField(max_length=256)  # 工作
    city = models.CharField(max_length=256)  # 城市
    salary = models.CharField(max_length=256)  # 雇佣
    url = models.CharField(max_length=256)  # 链接

    class Meta:
        db_table = 'zhipin'


class Zhilian(models.Model):
    id = models.IntegerField(primary_key=True)
    company = models.CharField(max_length=256)  # 公司
    job = models.CharField(max_length=256)  # 工作
    city = models.CharField(max_length=256)  # 城市
    salary = models.CharField(max_length=256)  # 雇佣
    url = models.CharField(max_length=256)  # 链接

    class Meta:
        db_table = 'zhilian'
