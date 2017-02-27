from django.shortcuts import render, redirect
from .models import *

def index(request):
	context = {
		'courses': Course.objects.all()
	}
	print context['courses']
	return render(request, "main_app/index.html", context)

def addcourse(request):
	if request.method == 'POST':
		print Course.objects.create(name=request.POST.get('name'), description=request.POST.get('description'))
	return redirect('/')

def destroycourse(request, id):
	context = {
		'course': Course.objects.get(id=id)
	}
	return render(request, "main_app/destroycourse.html", context)

def deletecourse(request, id):
	if request.method == 'POST':
		Course.objects.get(id=id).delete()
	return redirect('/')
