from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sport/(?P<sportname>\w{0,50})/$', views.sport, name='sport'),
    url(r'^calendar/athlete/(?P<athlete_id>\w+)/$',views.calendar, name='calendar'),
]