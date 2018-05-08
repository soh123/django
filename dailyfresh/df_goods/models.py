from django.db import models
from tinymce.models import HTMLField

class TypeInfo(models.Model):
	title=models.CharField(max_length=20,verbose_name='类别')
	isDelete=models.BooleanField(default=False,verbose_name='删除')
	def __str__(self):
		return str(self.title)

class GoodsInfo(models.Model):
	gtitle=models.CharField(max_length=20,verbose_name='名称')
	gpic=models.ImageField(upload_to='df_goods',verbose_name='图片')
	gprice=models.DecimalField(max_digits=5,decimal_places=2,verbose_name='价格')
	isDelete=models.BooleanField(default=False,verbose_name='删除')
	gunit=models.CharField(max_length=20,verbose_name='类别')
	gclick=models.IntegerField(verbose_name='点击量')
	gstores=models.IntegerField(verbose_name='库存')
	gsold=models.IntegerField(verbose_name='销售数量')
	gtips=models.CharField(max_length=100,verbose_name='简介')
	gcomment=models.CharField(max_length=200,verbose_name='评论')
	gcontent=HTMLField('宝贝详情')
	gtype=models.ForeignKey(TypeInfo,verbose_name='类别')
	gpush=models.BooleanField(default=False,verbose_name='推荐')
	def __str__(self):
		return str(self.gtitle)