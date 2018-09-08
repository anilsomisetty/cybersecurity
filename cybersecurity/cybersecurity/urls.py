from django.conf.urls import include,url
from django.contrib import admin
# from main import urls
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main/',include('main.urls'))
]
