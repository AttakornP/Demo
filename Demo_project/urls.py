from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Demo.views.home', name='home'),
    # url(r'^Demo/', include('Demo.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
