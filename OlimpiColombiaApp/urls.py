from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test', views.test, name='test'),
    url(r'^sport/(?P<sportname>\w{0,50})/$', views.sport, name='sport'),
]