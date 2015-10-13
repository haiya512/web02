from django.conf.urls import patterns, include, url
from web.views import *
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'py_web.views.home', name='home'),
    # url(r'^py_web/', include('py_web.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	(r'^$',index),
	(r'^monitor/$',monitor),
	(r'time/$',current_datetime),
	(r'^login/$',account_login),
        (r'^runCmd/$',runCmd),
        (r'^getCmdResult/$',getCmdResult),
        (r'^dashboard/$',dashboard),
        (r'^server_manager/$',server_manager),
        (r'^get_ip_list/$',get_ip_list),
	(r'^upload/$',upload),
)
