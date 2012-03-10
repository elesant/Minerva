from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('account.views',
    url(r'^login/', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^signup/$', 'signup', name='signup'),
    url(r'^people/$', 'people', name='people'),
    url(r'^people/(?P<username>\w+)/$', 'people')
)
