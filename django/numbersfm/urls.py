from django.conf.urls.defaults import patterns, include, url
import settings
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'core.views.home', name='home'),
    url(r'', include('radio.urls')),
    
    # url(r'^numbersfm/', include('numbersfm.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
