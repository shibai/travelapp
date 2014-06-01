from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf.urls import patterns, url, include
from rest_framework import routers



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^travelapp/', include('travelapp.urls')),
)

