from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app_sample.views.home', name='home'),
    url(r'^quick-text/$', 'app_sample.views.quick_text', name='quick_text'),
    url(r'^archives/$', 'app_sample.views.archives', name='archives'),
    url(r'^category/$', 'app_sample.views.category', name='category'),
    url(r'^signup/$', 'app_sample.views.signup', name='signup'),
    url(r'^signin/$', 'app_sample.views.signin', name='signin'),
    url(r'^about/$', 'app_sample.views.about', name='about'),
    # url(r'^blog/', include('blog.urls')),
)
