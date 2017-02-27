from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import re, bcrypt
from datetime import datetime
from django.utils.timezone import utc

class UserManager(models.Manager):
	EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

	def is_user_valid(self, request, fname, lname, email, password, passwordc):
		isValid = True
		if self.filter(email=email).first():
			messages.add_message(request, messages.INFO, 'The email address '+email+' is already registered')
			return False
		if len(fname) == 0 or len(lname) == 0 or len(email) == 0 or len(password) == 0 or len(passwordc) == 0:
			messages.add_message(request, messages.INFO, 'Please fill in all fields')
			return False
		if not fname.isalpha() or not lname.isalpha():
			isValid = False
			messages.add_message(request, messages.INFO, 'Your name should include only letters')
		if len(fname) < 2 or len(lname) < 2:
			isValid = False
			messages.add_message(request, messages.INFO, 'Your name should be at least 2 characters')
		if not UserManager.EMAIL_REGEX.match(email):
			isValid = False
			messages.add_message(request, messages.INFO, 'Invalid Email address')
		if len(password) < 8:
			isValid = False
			messages.add_message(request, messages.INFO, 'Your password should be 8 or more characters')
		if password != passwordc:
			isValid = False
			messages.add_message(request, messages.INFO, 'Your passwords must match')
		
		return isValid

	def login_user(self, request, email, password):
		if len(email) == 0 or len(password) == 0:
			messages.add_message(request, messages.INFO, 'Please fill in the email and password')
			return (False, None)
		if not UserManager.EMAIL_REGEX.match(email):
			messages.add_message(request, messages.INFO, 'Invalid Email address')
			return (False, None)
		user = self.filter(email=email).first()
		if user and bcrypt.hashpw(password.encode(), user.password.encode()) == user.password:
			return (True, user)
		messages.add_message(request, messages.INFO, 'The email and password did not match')
		return (False, user)

class AppointmentManager(models.Manager):
	def is_valid(self, request, date, time, tasks, update=False):
		if len(date) == 0 or len(time) == 0 or len(tasks) == 0:
			messages.add_message(request, messages.INFO, 'Please fill in all fields')
			return False
		dt = datetime.combine(datetime.strptime(date, '%Y-%m-%d'), datetime.strptime(time, '%H:%M').time())
		if dt < datetime.today():
			messages.add_message(request, messages.INFO, 'Please enter a current or future date and time')
			return False
		if not update:
			user = User.objects.filter(id=request.session['user_id'])
			if self.filter(datetime=dt,user=user).first():
				messages.add_message(request, messages.INFO, 'This date and time is already taken')
				return False
		return True

class User(models.Model):
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

class Secret(models.Model):
	secret = models.TextField(max_length=5555)
	user = models.ForeignKey(User, related_name='secrets')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def get_time_diff(self):
		now = datetime.utcnow().replace(tzinfo=utc)
		timediff = now - self.updated_at
		return timediff

class Like(models.Model):
	secret = models.ForeignKey(Secret, related_name='likes')
	user = models.ForeignKey(User, related_name='likes')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
