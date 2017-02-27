from django.shortcuts import render, redirect
from django.contrib import messages
import re
from .models import *

def index(request):
	context = {
		
	}
	return render(request, "main_app/index.html", context)

def process(request):
	if request.method == 'POST':
		email=request.POST.get('email')

		formValid = True
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

		if len(email) == 0:
			formValid = False
			messages.add_message(request, messages.INFO, 'Please enter an email address')
		else:
			if not EMAIL_REGEX.match(email):
				formValid = False
				messages.add_message(request, messages.INFO, 'Invalid Email address')

		if not formValid:
			return redirect('/')

		Email.objects.create(email=email)
		request.session['email'] = email
	return redirect('/emails')

def emails(request):
	context = {
		'emails': Email.objects.all()
	}
	return render(request, "main_app/emails.html", context)

def del_email(request, id):
	Email.objects.get(id=id).delete()
	return redirect('/emails')
