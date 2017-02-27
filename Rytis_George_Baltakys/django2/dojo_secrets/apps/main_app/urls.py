from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^secrets$', views.secrets),
    url(r'^secrets/(?P<id>\w+)/like/(?P<wherefrom>\w+)$', views.secrets_like),
    url(r'^secrets/(?P<id>\w+)/delete$', views.secrets_delete),
]
