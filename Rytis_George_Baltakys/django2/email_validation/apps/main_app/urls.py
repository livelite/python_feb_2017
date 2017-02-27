from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),  
    url(r'^emails$', views.emails),  
    url(r'^emails/delete/(?P<id>\w+)$', views.del_email),     
]
