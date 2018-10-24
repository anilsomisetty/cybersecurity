from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login,{'template_name': 'auth/login.html'},name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/',views.profile, name='profile'),
    url(r'^editprofile/',views.update_profile, name='update_profile'),
    url(r'^changepassword/',views.changepassword, name='changepassword'),
    url(r'^forgotpassword/',views.forgotpassword, name='forgotpassword'),
    url(r'^learn/', views.learn,name="learn"),
    url(r'^reversing/(?P<id>[0-9]+)$', views.reversing,name="reversing"),
    url(r'^forensics/(?P<id>[0-9]+)$', views.forensics,name="forensics"),
    url(r'^crypto/(?P<id>[0-9]+)$', views.crypto,name="crypto"),
    url(r'^web/(?P<id>[0-9]+)$', views.web,name="web"),
    url(r'^binary/(?P<id>[0-9]+)$', views.binary,name="binary"),
    url(r'^general/(?P<id>[0-9]+)$', views.general,name="general"),
    url(r'^practice/', views.practice,name="practice"),
    url(r'^add_articles/',views.add_articles, name='add_articles' ),
    url(r'^useshell/',views.shell, name='shell' ),
    # url(r'^user/',views.index, name='index' ), added as i changed redirect url after login
]

