from django.http import HttpResponse,HttpResponseForbidden,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.template import loader
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import PhotoDetails
from django.db import IntegrityError
from .forms import DocumentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = DocumentForm(request.POST,request.FILES)
			if form.is_valid():
				newdoc = PhotoDetails(docfile=request.FILES['docfile'],user=request.user,caption=form.cleaned_data['caption'])
				newdoc.save()
				return HttpResponseRedirect('#')
		else:
			form=DocumentForm()
		latest_photo_list = PhotoDetails.objects.filter(user=request.user).order_by('-upload_date')
		paginator = Paginator(latest_photo_list, 5)
		page = request.GET.get('page')
		try:
			photos = paginator.page(page)
		except PageNotAnInteger:
			photos = paginator.page(1)
		except EmptyPage:
			photos = paginator.page(paginator.num_pages)

		template = loader.get_template('photolist/index.html') #because u set app_dir = true
		context = {
	        'latest_photo_list': photos,
	        'username':request.user.first_name,
	        'form':form
	    }
		return HttpResponse(template.render(context, request))
	else:
		template = loader.get_template('photolist/login.html')
		print("You're not logged in")
		return HttpResponse(template.render(None, request))


def login_photogram(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		login(request, user)
		# Redirect to a success page.
		return HttpResponseRedirect('/photogram')
	else:
		template = loader.get_template('photolist/login.html')
		print("You're not logged in")
		return HttpResponse(template.render(None, request))

def register_pre(request):
	template = loader.get_template('photolist/register.html')
	return HttpResponse(template.render(None, request))

def register_post(request):
	username = request.POST['username']
	first_name = request.POST['first_name']
	last_name = request.POST['last_name']
	email = request.POST['email']
	password = request.POST['password']
	try:
		user = User.objects.create_user(username, email, password)
	except IntegrityError:
		print('error registering')
		return register_pre(request)
	user.last_name = last_name
	user.first_name = first_name
	user.save()
	print(user)

	#now lets login
	return login_photogram(request)

def delete(request):
	pid = request.GET.get('id')
	p=PhotoDetails.objects.filter(id=pid)
	p.delete()
	return HttpResponseRedirect('/photogram')

def edit(request):
	pid = request.GET.get('id')
	newcaption = request.GET.get('caption')
	p=PhotoDetails.objects.filter(id=pid).update(caption=newcaption)
	return HttpResponseRedirect('/photogram')


def logout_view(request):
	if request.user.is_authenticated:
		logout(request)
	template = loader.get_template('photolist/login.html')
	return HttpResponse(template.render(None, request))
