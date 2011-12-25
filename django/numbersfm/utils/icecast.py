from urlparse import urljoin
from urllib import urlencode
import requests
from django.conf import settings


def update_current_song(song_name):
    # ?mount=/listen&mode=updinfo&song=Archive+Stream
    url = urljoin(settings.ICECAST_SERVER, '/admin/metadata')
    data = {'mount': settings.ICECAST_MOUNTPOINT,
            'mode': 'updinfo',
            'song': song_name}
    url = '%s?%s' % (url, urlencode(data))
    r = requests.get(url, auth=(settings.ICECAST_ADMIN_USER,
                                settings.ICECAST_ADMIN_PASSWORD))
    
