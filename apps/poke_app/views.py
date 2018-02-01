# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from forms import *
from django.db.models import Sum
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	if request.method == 'POST':
		regForm = registerForm(request.POST)
		logForm = loginForm(request.POST)
	else:
		regForm = registerForm()
		logForm = loginForm()
	return render(request,'poke_app/index.html', {'regForm': regForm, 'logForm': logForm})

def user_create(request):
	errors = User.objects.register_validator(request.POST)
	if len(errors) == 0:
		x = User.objects.get(emai=request.POST['email'])
		request.session['regId'] = x.id
		p = Poke.objects.create(user=User.objects.get(id=request.session['id']))
		return redirect('/')
	else:
		for error in errors:
			messages.error(request, errors[error])
		return redirect('/')

def login(request):
	errors = User.objects.login_validator(request.POST)
	if len(errors) == 0:
		U = User.objects.get(email=request.POST['email'])
		request.session['email'] = U.email
		request.session['nam'] = U.name
		request.session['id'] = U.id
		return redirect('/pokes')
	else:
		for error in errors:
			messages.error(request, errors[error])
		return redirect('/')

def dashboard(request):

	context = {
	'my_pokes': Poke.objects.filter(poke_reciever=User.objects.get(email=request.session['email'])).order_by("-count"),
	'others_pokes': User.objects.exclude(email=request.session['email']).annotate(num_pokes=Sum('pokes_received__count'))
	}
	return render(request, 'poke_app/dashboard.html', context)

def logout(request):
	request.session.flush()
	return redirect('/')

def poke(request):
	Poke.objects.createPoke(sender=request.session['id'], receiver=request.POST['poke_receiver'])
	return redirect('/pokes')