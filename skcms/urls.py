from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^article/',include('articles.urls')),
    # Examples:
    # url(r'^$', 'skcms.views.home', name='home'),
    # url(r'^skcms/', include('skcms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('userprofile.urls')),
    url(r'^notifications/', include('notifications.urls')),

    url(r'^accounts/login/$', 'skcms.views.login'),
    url(r'^accounts/auth/$', 'skcms.views.auth_view'),
    url(r'^accounts/logout/$', 'skcms.views.logout'),
    url(r'^accounts/loggedin/$', 'skcms.views.loggedin'),
    url(r'^accounts/invalid/$', 'skcms.views.invalid_login'),

    url(r'^accounts/create_user/$', 'skcms.views.create_user'),
    url(r'^accounts/create_user_success/$', 'skcms.views.create_user_success'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
