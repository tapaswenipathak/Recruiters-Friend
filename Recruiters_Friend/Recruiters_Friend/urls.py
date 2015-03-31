from django.conf.urls import patterns, include, url
from django.contrib import admin
from jd.views import base, rating_calculation, questionnaire 
from candidates.views import base1, api_call

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'common.views.home', name='home'),
    url(r'^about/', 'common.views.about', name='about'),
    url(r'^jd/', base),
    url(r'^rating/', rating_calculation),
    url(r'^questions/',questionnaire),
    url(r'^candidates/',base1),
    url(r'^candidates_list/',api_call),   
    url(r'^admin/', include(admin.site.urls)),

)
