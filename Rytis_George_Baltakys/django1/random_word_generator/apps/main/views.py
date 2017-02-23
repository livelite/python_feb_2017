from django.shortcuts import render, HttpResponse, redirect
import datetime, time, random, string


# CONTROLLER

# Create your views here.
def index(request):

	# session
	if 'counter' not in request.session:
		request.session['counter'] = 0
	else:
		request.session['counter'] += 1

	data = {
		'randomWord' : ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(14)]),
		'counter' : request.session['counter']
	}
	return render(request, "main/index.html", data)

def newword(request):
	if request.method == "POST":
		print '*' * 50
		print request
		print '*' * 50

	return redirect("/")
