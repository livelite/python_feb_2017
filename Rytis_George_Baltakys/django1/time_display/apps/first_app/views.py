from django.shortcuts import render, HttpResponse
import datetime
import time

# CONTROLLER

# Create your views here.
def index(request):

	data = {
		'date': datetime.date.today(),
		'time': time.strftime('%I:%M:%S')
	}
	return render(request, "first_app/index.html", data)

def show(request):
	print request.method
	return render(request, "first_app/users.html")
