from django.shortcuts import render, HttpResponse, redirect
import datetime, time, random, string


# CONTROLLER

# Create your views here.
def index(request):

	context = {
		'randomWord' : ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(14)]),
		'counter' : request.session['counter']
	}
	return render(request, "main/index.html", context)

def processForm(request):
	# session
	if 'counter' not in request.session:
		request.session['counter'] = 0
	else:
		request.session['counter'] += 1

	if request.method == "POST":
		request.session['name'] = request.POST.get('name')
		request.session['language'] = request.POST.get('language')
		request.session['location'] = request.POST.get('location')
		request.session['comment'] = request.POST.get('comment')
		return redirect("/success")

	return redirect("/")

def success(request):

	return render(request, "main/success.html")

