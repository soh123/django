from django.shortcuts import render

def cart(request):
	uid=request.session['user_id']
	carts=CartInfo.objects.filter(user_id=uid)
	context={'title':'购物车','page_name':1,'cart':carts}
	return render(request,'df_cart/cart/html',context)
