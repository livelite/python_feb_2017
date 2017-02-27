from django.shortcuts import render, redirect
from .models import *
import bcrypt
from django.db.models import Count
from datetime import datetime

def index(request):
	#request.session.clear()
	context = {
	}
	if 'user_id' in request.session:
		current_user = User.objects.get(id=request.session['user_id'])
		secrets = Secret.objects.annotate(like_count=Count('likes')).order_by('-created_at')[:5]
		
		for secret in secrets:
			if secret.user == current_user:
				secret.mine = True
			else:
				secret.mine = False
			secret.time_elapsed = humanizeTimeDiff(secret.get_time_diff())
		context['secrets'] = secrets
	return render(request, "main_app/index.html", context)

def register(request):
	if request.method == 'POST':
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		email = request.POST.get('email')
		password = request.POST.get('pass')
		passwordc = request.POST.get('passc')

		if User.objects.is_user_valid(request, fname, lname, email, password, passwordc):
			# generate password hash
			pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

			# form data is Valid, save user to database, and log them in
			user = User.objects.create(email=email, first_name=fname, last_name=lname, password=pw_hash)
			request.session['user_id'] = user.id
			request.session['user_email'] = user.email
			request.session['user_first_name'] = user.first_name
			request.session['user_last_name'] = user.last_name

	return redirect('/')

def login(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('pass')

		login = User.objects.login_user(request, email, password)
		if login[0]:
			# log user in
			request.session['user_id'] = login[1].id
			request.session['user_email'] = login[1].email
			request.session['user_first_name'] = login[1].first_name
			request.session['user_last_name'] = login[1].last_name

	return redirect('/')

def logout(request):
	request.session.clear()
	return redirect('/')

def secrets(request):
	if request.method == 'POST':
		secret = request.POST.get('secret')
		current_user = User.objects.get(id=request.session['user_id'])
		Secret.objects.create(secret=secret, user=current_user)
	elif request.method == 'GET':
		current_user = User.objects.get(id=request.session['user_id'])
		secrets = Secret.objects.annotate(like_count=Count('likes')).order_by('-like_count')
		
		for secret in secrets:
			if secret.user == current_user:
				secret.mine = True
			else:
				secret.mine = False
		context = {
		}
		if 'user_id' in request.session:
			user = User.objects.filter(id=request.session['user_id'])
			context['secrets'] = secrets
		return render(request, "main_app/pop_secrets.html", context)
	return redirect('/')

def secrets_like(request, id, wherefrom):
	current_user = User.objects.filter(id=request.session['user_id']).first()
	secret = Secret.objects.filter(id=id).first()
	# if like already exists
	if Like.objects.filter(secret=secret, user=current_user).first():
		# unlike
		Like.objects.filter(secret=secret, user=current_user).delete()
	else:
		# like
		Like.objects.create(secret=secret, user=current_user)
	if wherefrom == 'main':
		wherefrom = ''
	return redirect('/' + wherefrom)

def secrets_delete(request, id):
	Secret.objects.get(id=id).delete()
	return redirect('/')

def humanizeTimeDiff(timeDiff):
	"""
	Returns a humanized string representing time difference
	The output rounds up to days, hours, minutes, or seconds.
	4 days 5 hours returns '4 days'
	0 days 4 hours 3 minutes returns '4 hours', etc...
	"""
	days = timeDiff.days
	hours = timeDiff.seconds/3600
	minutes = timeDiff.seconds%3600/60
	seconds = timeDiff.seconds%3600%60
	str = ""
	tStr = ""
	if days > 0:
			if days == 1:   tStr = "day"
			else:           tStr = "days"
			str = str + "%s %s" %(days, tStr)
			return str
	elif hours > 0:
			if hours == 1:  tStr = "hour"
			else:           tStr = "hours"
			str = str + "%s %s" %(hours, tStr)
			return str
	elif minutes > 0:
			if minutes == 1:tStr = "min"
			else:           tStr = "mins"           
			str = str + "%s %s" %(minutes, tStr)
			return str
	elif seconds > 0:
			if seconds == 1:tStr = "sec"
			else:           tStr = "secs"
			str = str + "%s %s" %(seconds, tStr)
			return str
	else:
			return 'very recently'
