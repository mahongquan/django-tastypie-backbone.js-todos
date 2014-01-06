from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from tastypie.api import Api
from api.resources import *
v1_api = Api(api_name='v1')
v1_api.register(TodoResource())
urlpatterns = patterns('',
    url(r'^$', 'mysite.views.index'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),#/api/v1/contact/?format=json
)
urlpatterns += staticfiles_urlpatterns()
