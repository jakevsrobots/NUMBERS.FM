from urlparse import urljoin
import requests
from django.conf import settings


def update_current_song(song_name):
    url = urljoin(settings.ICECAST_SERVER, '/admin/metadata')
    r = requests.get(url, auth=(settings.ICECAST_ADMIN_USER,
                                settings.ICECAST_ADMIN_PASSWORD))

    # todo
