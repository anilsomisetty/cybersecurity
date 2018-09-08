from django.conf.urls import url
from django.contrib import admin
from .import views as main_views
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
urlpatterns = [
	url(r'^login/$', auth_views.login,{'template_name': 'main/login.html'},name='login'),
    url(r'^signup/$',main_views.signup,name='signup')
]