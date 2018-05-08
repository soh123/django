from django.db import models

class CartInfo(models.Model):
	user=models.FroeignKey('df_user.UserInfo')
	goods=models.FroeignKey('df_goods.GoodsInfo')
	num=models.IntegerField()
