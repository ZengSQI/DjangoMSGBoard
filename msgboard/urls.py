from django.conf.urls import url

from . import views

app_name = 'msgboard'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/$', views.post, name='post'),
    url(r'^(?P<msg_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<msg_id>[0-9]+)/comment/$', views.comment, name='comment'),
]
