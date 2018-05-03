from . import views
from django.conf.urls import url,include

urlpatterns=[
	url(r'^register/',views.register),
	url(r'^register_handle/',views.register_handle),
	url(r'^login/$',views.login),
]