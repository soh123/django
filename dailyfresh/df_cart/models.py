from django.db import models
from df_user.models import *
from df_goods.models import *

class CartInfo(models.Model):
	user=models.ForeignKey('df_user.UserInfo',verbose_name='用户ID')
	goods=models.ForeignKey('df_goods.GoodsInfo',verbose_name='商品ID')
	num=models.IntegerField(verbose_name='数量')
def __str__(self):
		return str(self.uname)