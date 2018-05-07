from django.db import models

class UserInfo(models.Model):
	uname=models.CharField(max_length=20,verbose_name='用户名')
	upwd=models.CharField(max_length=100)
	uemail=models.CharField(max_length=40,verbose_name='电子邮箱')
	urecipient=models.CharField(max_length=20,default='',verbose_name='收件人')
	uaddress=models.CharField(max_length=100,default='',verbose_name='地址')
	uzip=models.CharField(max_length=6,default='',verbose_name='邮编')
	uphone=models.CharField(max_length=11,default='',verbose_name='手机')
