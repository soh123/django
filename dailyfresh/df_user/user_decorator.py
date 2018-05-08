#coding=utf-8
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

def idlogin(func):
	def login_fun(req,*args,**kw):
		if req.session.has_key('user_id'):
			return func(req,*args,**kw)
		else:
			red=HttpResponseRedirect('/user/login/')
			red.set_cookie('url',req.get_full_path())
			return red
	return login_fun