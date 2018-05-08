#coding=utf-8
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.hashers import make_password,check_password
from django.http import JsonResponse,HttpResponseRedirect
from . import user_decorator
from df_goods.models import *

def register(request):
	return render(request,'df_user/register.html')		

def register_handle(request):
	#接收用户输入
	post=request.POST
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

def register_exist(request):
	uname=request.GET['uname']
	count = UserInfo.objects.filter(uname=uname).count()
	#exist_username = UserInfo.objects.exists('uname'=uname)
	return JsonResponse({'count':count})
	#return exist_username

def login(request):
	uname=request.COOKIES.get('uname','')
	context={'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
	return render(request,'df_user/login.html',context)

def logout(request):
	request.session.flush()
	return redirect('/')

def login_handle(request):
	post = request.POST
	uname=post.get('username')
	upwd=post.get('pwd')
	rmb=post.get('rmb',0)

	users=UserInfo.objects.filter(uname=uname)
	url=request.COOKIES.get('url','/')

	if len(users)==1:
		if check_password(upwd,users[0].upwd):
			red = HttpResponseRedirect(url)

			if rmb !=0:
				red.set_cookie('uname',uname)
			else:
				red.set_cookie('uname','',max_age=-1)
			request.session['user_id']=users[0].id
			request.session['user_name']=uname
			request.session.set_expiry(0)
			return red
		else:
			context = {'title':'用户登录','error_name':0,'error_pwd':1,'uname':uname,'upwd':upwd}
			return render(request, 'df_user/login.html',context)
	else:
		context = {'title':'用户登录','error_name':1,'error_pwd':0,'uname':uname,'upwd':upwd}
		return render(request, 'df_user/login.html',context)

@user_decorator.idlogin
def info(request):
	user_email=UserInfo.objects.get(id=request.session['user_id']).uemail

	# goods_ids=request.COOKIES.get('goods_ids','')
	# goods_ids1=goods_ids.split(',')
	# goods_list=[]
	# for goods_id in goods_ids1:
	# 	goods_list.append(GoodsInfo.objects.get(id=int(goods_id)))

	#context={'title':'用户中心','user_email':user_email,'user_name':request.session['user_name'],'page_name':1,'goods_list':goods_list}
	context={'title':'用户中心','user_email':user_email,'user_name':request.session['user_name'],'page_name':1}

	return render(request,'df_user/user_center_info.html',context)

@user_decorator.idlogin
def order(request):
	return render(request,'df_user/user_center_order.html')

@user_decorator.idlogin
def site(request):
	return render(request,'df_user/user_center_site.html')



