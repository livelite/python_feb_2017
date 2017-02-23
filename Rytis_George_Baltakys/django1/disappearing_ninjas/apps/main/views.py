from django.shortcuts import render, HttpResponse, redirect
import datetime, time, random, string


# CONTROLLER

# Create your views here.
def index(request):
	return render(request, "main/index.html")

def ninja(request, color):

	ninja = ''
	
	if color == 'blue':
		ninja = 'leonardo'
	elif color == 'orange':
		ninja = 'michelangelo'
	elif color == 'red':
		ninja = 'raphael'
	elif color == 'purple':
		ninja = 'donatello'
	else:
		ninja = 'notapril'

	context = {
		'ninja': ninja
	}

	return render(request, "main/ninja.html", context)

def allNinjas(request):

	return render(request, "main/allninjas.html")
