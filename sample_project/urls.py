from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sample_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r"^", include('app_sample.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
