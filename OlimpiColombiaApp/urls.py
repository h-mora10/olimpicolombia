from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^accounts/login/$', auth_views.login, name='account_login'),
    url(r'^sport/(?P<sport_id>\w+)/$', views.sport, name='sport'),
    url(r'^calendar/athlete/(?P<athlete_id>\w+)/$', views.calendar, name='calendar'),
    url(r'^calendar/athlete/video/(?P<athlete_id>\w+)/$', views.latest_video_src, name='latestVideo'),
    url(r'^logged_out', views.logout, name='logout')

]