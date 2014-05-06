from django.conf.urls import patterns, include, url


urlpatterns = patterns('vmmanager.views',
    # Examples:
    # url(r'^$', 'cloudfront.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'index'),
    url(r'^create/$', 'create'),
    url(r'^status/(?P<vmname>[^/]+)/$', 'status'),
)
