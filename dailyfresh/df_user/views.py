#coding=utf-8
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.hashers import make_password

def register(req):
	return render(req,'df_user/register.html')		

def register_handle(req):
	#接收用户输入
	post=req.POST
	uname=post.get('user_name')
	upwd=post.get('pwd')
	uemail=post.get('email')
	upwd2=post.get('cpwd')

	#print(uname,upwd,uemail)
	#再次验证两次密码
	if upwd2 != upwd:
		return redirect('/user/register/')

	#密码加密	
	upwd3=make_password(upwd)
	

	#创建对象
	user = UserInfo()
	user.uname = uname
	user.upwd = upwd3
	user.uemail = uemail
	user.save()
	#转登录页面
	return redirect('/user/login/')

def register_exist(req):
	uname=req.GET.get('uname')
	count = UserInfo.object.filter(uname=uname).count()
	return JsonResponse({'count':count})

def login(req):
	uname=req.COOKIES.get('uname','')
	context={'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
	return render(req,'df_user/login.html',context)

	

