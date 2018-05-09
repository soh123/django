from django.contrib import admin
from .models import *

class CartInfoAdmin(admin.ModelAdmin):
	list_per_page = 20
	list_display = ['user','goods','num']
admin.site.register(CartInfo,CartInfoAdmin)

