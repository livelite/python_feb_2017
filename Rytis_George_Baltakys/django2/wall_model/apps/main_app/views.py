from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
	User.objects.create(first_name="Rytis", last_name="Baltakys",email="Rytis", password="Baltakys")
	user = User.objects.all()
	print user
	return render(request, "main_app/index.html")