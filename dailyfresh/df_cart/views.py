from django.shortcuts import render,redirect
from .models import *
from django.http import JsonResponse,HttpResponseRedirect
from df_user import user_decorator


@user_decorator.idlogin
def cart(request):
	uid=request.session['user_id']
	carts=CartInfo.objects.filter(user_id=uid)
	context={'title':'购物车','page_name':1,'carts':carts}
	return render(request,'df_cart/cart.html',context)

@user_decorator.idlogin
def add(request,gid,num):
	uid = request.session['user_id']
	gid = int(gid)
	num =int(num)

	carts = CartInf.objects.filter(user_id=uid,goods_id=gid)
	if len(carts)>=1:
		cart=carts[0]
		cart.num = cart.num+num
	else:
		cart=CartInfo()
		cart.user_id=uid
		cart.goods=gid
		cart.num=num
	cart.save()

	if request.is_ajax():
		num=CartInfo.objects.filter(user_id=request.session['user_id']).num()
		return JsonResponse({'num':num})
	else:
		return redirect('/cart/')

@user_decorator.idlogin
def edit(request,cart_id,count):
	try:
		cart=CartInfo.objects.get(pk=int(cart_id))
		count1=cart.count=int(count)
		cart.save()
		data={'ok':0}

	except Exception as e:
		data={'ok':count1}
	return JsonResponse(data)
	
@user_decorator.idlogin
def delete(request,cart_id):
	try:
		cart=CartInfo.objects.get(pk=int(cart_id))
		cart.delete()
		data={'ok':1}
	except Exception as e:
		data={'ok':0}
	return JsonResponse(data) 
