from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
     url(r'^testapp1/', include('testapp1.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
