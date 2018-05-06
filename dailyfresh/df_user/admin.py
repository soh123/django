from django.contrib import admin
from .models import *

class UserInfoAdmin(admin.ModelAdmin):
	list_per_page = 15
	list_display = ['id','uname','uemail','urecipient','uaddress','uzip','uphone']

admin.site.register(UserInfo,UserInfoAdmin)
