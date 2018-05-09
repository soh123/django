from django.db import models
from df_user.models import *
from df_goods.models import *

class CartInfo(models.Model):
	user=models.ForeignKey('df_user.UserInfo')
	goods=models.ForeignKey('df_goods.GoodsInfo')
	num=models.IntegerField()
