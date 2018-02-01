from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^users/create$', views.user_create),
	url(r'^pokes$', views.dashboard),
	url(r'^login$', views.login),
	url(r'^logout$', views.logout),
	url(r'^poke', views.poke),
]