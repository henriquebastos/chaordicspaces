# coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'chaordicspaces.core.views.home', name='home'),
    url(r'^subscription/new/$', 'chaordicspaces.core.views.subscription_new', name='subscription_new'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', kwargs={'next_page': '/'}, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
)
