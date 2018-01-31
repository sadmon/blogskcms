from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^show_all/$', 'articles.views.articles'),
	url(r'^(?P<article_id>\d+)/$', 'articles.views.article'),
	url(r'^(?P<article_id>\d+)/add_comment/$', 'articles.views.add_comment'),
)