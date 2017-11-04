from django.conf.urls import url, include

from . import views
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	url('', include('social_django.urls', namespace='social')),
	url(r'^login/$', redirect, {'url': '/login/google-oauth2'}),
	url(r'^$', views.post_list, name='post_list'),
	url(r'^posts$', views.post_all, name='post_all'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/delete/$', views.post_delete, name='post_delete'),
	url(r'^logout$', views.logout_view, name='logout_view'),
]