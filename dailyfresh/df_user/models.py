from django.db import models

class UserInfo(models.Model):
	uname=models.CharField(max_length=20)
	upwd=models.CharField(max_length=100)
	uemail=models.CharField(max_length=40)
	urecipient=models.CharField(max_length=20,default='')
	uaddress=models.CharField(max_length=100,default='')
	uzip=models.CharField(max_length=6,default='')
	uphone=models.CharField(max_length=11,default='')
