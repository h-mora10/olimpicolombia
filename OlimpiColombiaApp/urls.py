from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sport/(?P<sport_id>\w+)/$', views.sport, name='sport'),
    url(r'^calendar/athlete/(?P<athlete_id>\w+)/$',views.calendar, name='calendar'),
    url(r'^calendar/athlete/video/(?P<athlete_id>\w+)/$',views.latest_video_src, name='latestVideo'),
]