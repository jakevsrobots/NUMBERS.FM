from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^privacy-policy/$', 'pages.views.page_detail_view', {
            'page_name': "Privacy Policy and Terms of Service"
            },
        name='privacy-policy'),
)
