from django.db import models

class TypeInfo(models.Model):
	title=models.CharField(max_length=20)
	isDelete=models.BooleanField(default=False)
	def __str__(self):
		return self.title.encode('utf-8')

class GoodsInfo(models.Model):
	gtitle=models.CharField(max_length=20)
	gpic=models.ImageField(upload_to='df_goods')
	gprice=models.DecimalField(max_digits=5,decimal_places=2)
	isDelete=models.BooleanField(default=False)
	gunit=models.CharField(max_length=20)
	gclick=models.IntegerField()
	gstores=models.IntegerField()
	gsold=models.IntegerField()
	gtips=models.CharField(max_length=100)
	gcomment=models.CharField(max_length=200)
	gcontent=models.TextField()
	gtype=models.ForeignKey(TypeInfo)
	gpush=models.BooleanField(default=False)
	def __str__(self):
		return self.gtitle.encode('utf-8')