from django.db import models
# Create your models here.
class Customer(models.Model):
    # 客户名称
    name = models.CharField(max_length=200)

    # 联系电话
    phonenumber = models.IntegerField(max_length=20)

    # 地址
    address = models.CharField(max_length=200)

    # qq
    qq = models.CharField(max_length=20, null=True, blank=True)