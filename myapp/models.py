from django.db import models


# Create your models here.


class score(models.Model):
    score = models.IntegerField('分数')
    user_name = models.CharField('客户端id', max_length=64)