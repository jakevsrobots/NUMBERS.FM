import commands
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
    
# todo: port these away from the commands module to subprocess, etc.
def start_archives():
    if commands.getoutput('pidof ices'):
        return

    commands.getoutput('start_ices.sh')
    
def stop_archives():
    commands.getoutput('stop_ices.sh')
    
def archive_stream_is_running():
    try:
        ices_pid = int(commands.getoutput('pidof ices'))
        return True
    except ValueError:
        return False
