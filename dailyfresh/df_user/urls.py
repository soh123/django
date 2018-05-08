from . import views
from django.conf.urls import url,include

urlpatterns=[
	url(r'^register/',views.register),
	url(r'^$',views.info),
	url(r'^register_handle/',views.register_handle),
	url(r'^login/$',views.login),
	url(r'^login_handle/',views.login_handle),
	url(r'^info/$',views.info),
	url(r'^register_exist/',views.register_exist),
	url(r'^info/',views.info),
	url(r'^order/',views.order),
	url(r'^site/',views.site),
	url(r'^logout/$',views.logout),
]