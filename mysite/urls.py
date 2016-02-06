from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

from .views import register

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/', login, {'template_name': 'login.html'}),
    url(r'^accounts/logout/', logout, {'template_name': 'logout.html'}),
    url(r'^accounts/register/', register),
    url(r'^msgboard/', include('msgboard.urls')),
]
