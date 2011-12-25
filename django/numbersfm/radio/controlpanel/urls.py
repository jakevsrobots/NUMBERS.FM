from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout


urlpatterns = patterns(
    'radio.controlpanel.views',

    url('^$', 'dashboard', name='dashboard'),
    url('^login/$', login, name='login'),
    url('^logout/$', logout, name='logout')
)
