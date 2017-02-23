from django.shortcuts import render, HttpResponse, redirect
import datetime, time, random, string


# CONTROLLER

# Create your views here.
def index(request):
	# get or initialize session variables
	if 'gold' not in request.session:
		request.session['gold'] = 0
		request.session['win'] = 0
		request.session['where'] = ''
		request.session['output'] = []

	return render(request, "main/index.html")

def process(request):
	if request.method == "POST":
		# reset game
		if request.POST.get('reset'):
			request.session.delete()
			return redirect('/')

		if request.POST.get('farm'):
				request.session['win'] = random.randrange(10, 21)
				request.session['where'] = 'farm'
		if request.POST.get('cave'):
				request.session['win'] = random.randrange(5, 11)
				request.session['where'] = 'cave'
		if request.POST.get('house'):
				request.session['win'] = random.randrange(2, 6)
				request.session['where'] = 'house'
		if request.POST.get('casino'):
				request.session['win'] = random.randrange(-50, 51)
				request.session['where'] = 'casino'

		request.session['gold'] += request.session['win']
		request.session['winDisplay'] = abs(request.session['win'])

		activity = ''
		if request.session['win'] > 0:
			activity += '<span class="gold">Eearned ' + str(request.session['win']) + ' gold from the ' + str(request.session['where'])
		else:
			activity += '<span class="loss">Lost ' + str(abs(request.session['win'])) + ' gold from the ' + str(request.session['where']) + '. Ouch..'
		activity += '! (' + time.asctime( time.localtime(time.time()) ) + ')</span><br>'

		request.session['output'].insert(0, activity)
	
	return redirect('/')

