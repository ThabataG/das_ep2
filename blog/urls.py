from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.publication_list),
	url(r'^publication/(?P<pk>[0-9]+)/$', views.publication_detail),
	url(r'^publication/new/$', views.publication_new, name='publication_new'),
	url(r'^publication/(?P<pk>[0-9]+)/edit/$', views.publication_edit, name='publication_edit'),
]
