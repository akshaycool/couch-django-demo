from django.conf.urls import patterns, include, url

from django.contrib import admin
from couch_docs.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'couch_django_demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^doc/(?P<id>\w+)/', detail),
    url(r'^$',index),
)
