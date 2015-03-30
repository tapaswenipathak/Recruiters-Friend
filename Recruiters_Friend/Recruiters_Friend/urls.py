from django.conf.urls import patterns, include, url
from django.contrib import admin
from jd.views import base, rating_calculation 

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'common.views.home', name='home'),
    url(r'^about/', common.views.about, name='about'),
    url(r'^jd/', base),
    url(r'^rating/', rating_calculation),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    

)
