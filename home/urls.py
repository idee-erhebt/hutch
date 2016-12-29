from django.conf.urls import url
from . import views

app_name='home'
urlpatterns=[
    url(r'^$',views.index,name='firstpage'),
    url(r'^schedule/', views.schedule, name='secondpage'),
    url(r'^venue/$', views.venue, name='thirdpage'),
    url(r'^dashboard/$', views.dashboard, name='forthpage'),
    url(r'^submittion/$', views.submitit, name='fifthpage'),
    url(r'^ideainput/$', views.submitit, name='fifthpage1'),
    url(r'^regis/(?P<registration_id>[0-9]+)$', views.registration, name='regis'),
    url(r'^forum/(?P<forum_id>[0-9]+)$', views.forum, name='forum'),
    url(r'^forumed/(?P<forum_id>[0-9]+)$', views.forumed, name='forumed'),
    url(r'^getme/(?P<forum_id>[0-9]+)$', views.getting, name='got'),
]