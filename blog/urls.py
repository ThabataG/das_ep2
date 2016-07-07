from django.conf.urls import include, url
from . import views
from django.contrib import admin

urlpatterns = [
	url(r'^$', views.publication_list, name='publication_list'),
	url(r'^publication/(?P<pk>[0-9]+)/$', views.publication_detail),
	url(r'^publication/new/$', views.publication_new, name='publication_new'),
	url(r'^publication/(?P<pk>[0-9]+)/edit/$', views.publication_edit, name='publication_edit'),
    url(r'^admin/', include(admin.site.urls) , name='admin'),
    url(r'^contact/$', views.form_contact, name='contact'),
    url(r'^contact/thanks/$', views.contact_thanks, name='thanks'),
]
