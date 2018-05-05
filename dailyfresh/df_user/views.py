#coding=utf-8
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.hashers import make_password,check_password
from django.http import JsonResponse,HttpResponseRedirect

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
	uname=req.GET['uname']
	count = UserInfo.objects.filter(uname=uname).count()
	#exist_username = UserInfo.objects.exists('uname'=uname)
	return JsonResponse({'count':count})
	#return exist_username

def login(req):
	uname=req.COOKIES.get('uname','')
	context={'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
	return render(req,'df_user/login.html',context)

def login_handle(req):
	post = req.POST
	uname=post.get('username')
	upwd=post.get('pwd')
	rmb=post.get('rmb',0)

	users=UserInfo.objects.filter(uname=uname)

	if len(users)==1:
		if check_password(upwd,users[0].upwd):
			red = HttpResponseRedirect('/user/info/')

			if rmb !=0:
				red.set_cookie('uname',uname)
			else:
				red.set_cookie('uname','',max_age=-1)
			req.session['user_id']=users[0].id
			req.session['user_name']=uname
			return red
		else:
			context = {'title':'用户登录','error_name':0,'error_pwd':1,'uname':uname,'upwd':upwd}
			return render(req, 'df_user/login.html',context)
	else:
		context = {'title':'用户登录','error_name':1,'error_pwd':0,'uname':uname,'upwd':upwd}
		return render(req, 'df_user/login.html',context)

def info(req):
	return render(req,'df_user/user_center_info.html')

def order(req):
	return render(req,'df_user/user_center_order.html')

def site(req):
	return render(req,'df_user/user_center_site.html')



