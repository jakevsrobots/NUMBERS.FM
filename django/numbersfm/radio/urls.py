from django.conf.urls.defaults import patterns, include, url
from views import ShowDetailView

urlpatterns = patterns(
    '',
    url(r'^shows/(?P<slug>[-_\w]+)/$', ShowDetailView.as_view(
            template_name='radio/show_detail.html',
            context_object_name='show'
            ),
        name='radio-show-detail'),
)
