from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index), # And now we use include to pull in our first_app.urls...
	url(r'^newword$', views.newword) # And now we use include to pull in our first_app.urls...
]
