# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import websocketserver
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from .models import Userpost
from .forms import Postform, Deleteform
from django.contrib import auth
from django.http import HttpResponse

# Create your views here.

def post_list(request):
	latest_userpost_list = Userpost.objects.order_by('-pub_date')[:5]
	context = {'latest_userpost_list': latest_userpost_list}
	return render(request, 'microblog/post_list.html', context)

def post_all(request):
	latest_userpost_list = Userpost.objects.order_by('-pub_date')
	context = {'latest_userpost_list': latest_userpost_list}
	return render(request, 'microblog/post_all.html', context)

def post_detail(request, pk):
	userpost = get_object_or_404(Userpost, pk=pk)
	context = {'userpost': userpost}
	return render(request, 'microblog/post_detail.html', context)

def post_new(request):
	if request.method == "POST" and request.is_ajax():
		is_author = Userpost(author = request.user)
		form = Postform(request.POST, instance = is_author)
		data = {k: v for k, v in request.POST.items()}
		if form.is_valid():
			data.update({'author' : request.user.username, 'pub_date' : str( timezone.now() ), 'success': True})
			form.save()
			# return redirect('post_list')

			return HttpResponse(json.dumps(data))
	else:
		form = Postform()
		context = {'form': form}
		return render(request, 'microblog/post_edit.html', context)


def post_delete(request,pk):
	userpost_to_delete = get_object_or_404(Userpost, pk=pk)
	if request.method == 'GET':
		form = Deleteform(request.POST, instance=userpost_to_delete)
		if form.is_valid(): 
			userpost_to_delete.delete()
			return redirect('post_list')
	else:
		form = Deleteform(instance=userpost_to_delete)
	context = {'form': form}
	return render(request, 'microblog/post_list.html', context)

def logout_view(request):
  auth.logout(request)
  # Redirect to the login page.
  return redirect('/microblog')
