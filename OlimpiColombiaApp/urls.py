from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views

# Example for crud standard
# GET     /api/v1/user           UserController :index
# GET     /api/v1/user/:id/edit  UserController :edit
# GET     /api/v1/user/new       UserController :new
# GET     /api/v1/user/:id       UserController :show
# POST    /api/v1/user           UserController :create
# PATCH   /api/v1/user/:id       UserController :update
# PUT     /api/v1/user/:id       UserController :update
# DELETE  /api/v1/user/:id

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^indexJSON', views.indexJSON, name='indexJSON'),
    url(r'^accounts/login/$', auth_views.login, name='account_login'),
    url(r'^sport/', views.sport, name='sport'),
    url(r'^sportJSON/(?P<sport_id>\w+)/$', views.sportJSON, name='sport'),
    url(r'^calendar/athlete/(?P<athlete_id>\w+)/$', views.calendar, name='calendar'),
    url(r'^calendar/athlete/video/(?P<athlete_id>\w+)/$', views.latest_video_src, name='latestVideo'),
    url(r'^logged_out', views.logout, name='logged_out'),
    url(r'^accounts/registration/$', views.register_student, name='register'),
    url(r'^student/(?P<student_uid>\w+)/$', views.show_student_by_uid, name='show_student_by_uid'),


]