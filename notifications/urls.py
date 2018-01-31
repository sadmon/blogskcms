from django.conf.urls import patterns, include, url

urlpatterns = patterns('notifications.views',
	url(r'^show/(?P<notification_id>\d+)/$', 'show_notification'),
	url(r'^delete/(?P<notification_id>\d+)/$', 'delete_notification'),
)