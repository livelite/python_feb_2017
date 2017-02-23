from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index), # And now we use include to pull in our first_app.urls...
	url(r'^process$', views.processForm),
	url(r'^success$', views.success),
]
