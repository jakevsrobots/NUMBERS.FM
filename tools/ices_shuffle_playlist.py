"""
A module used by `ices` to randomly play tracks from a folder.
"""

import os, random
from mutagen.easyid3 import EasyID3

# ----------------------
# Playlist manager class
# ----------------------
class PlaylistManager(object):
    @classmethod
    def get_manager(cls, *args, **kwargs):
        if not hasattr(cls, '_manager'):
            cls._manager = cls(*args, **kwargs)
            
        return cls._manager
    
    def __init__(self, archive_base_dir=None, num_tracks_to_count=10):
        if archive_base_dir is None:
            if "RADIO_ARCHIVES_PATH" in os.environ:
                archive_base_dir = os.environ['RADIO_ARCHIVES_PATH']
            else:
                # a sensible default?
                archive_base_dir = '/opt/mp3'

        self.archive_base_dir = archive_base_dir
        self.num_tracks_to_count = num_tracks_to_count
        self.recently_played_tracks = []
        self.now_playing = None

    def record_played_track(self, track):
        self.now_playing = track
        self.recently_played_tracks.insert(0, track)
        self.recently_played_tracks = self.recently_played_tracks[self.num_tracks_to_count:]

    def get_random_track(self):
        music_files = [
            os.path.join(self.archive_base_dir, x) \
                for x in os.listdir(self.archive_base_dir) \
                if os.path.splitext(x)[1].lower() == '.mp3'
        ]

        track = None
        counter = 0
        limit = len(music_files)
        while counter < limit:
            counter += 1
            track = random.choice(music_files)
            if track not in self.recently_played_tracks:
                break

        if not track:
            track = random.choice(music_files)

        self.record_played_track(track)
        return os.path.join(self.archive_base_dir, track)

    def get_metadata(self):
        print "get metadata"
        if self.now_playing:
            data = EasyID3(self.now_playing)
            metadata = '%s -- %s [NUMBERS.FM archive stream]' % (data['artist'][0], data['title'][0])
        else:
            metadata = 'NUMBERS.FM'

        print "md", metadata
        return metadata

# ----------------------
# Ices hooks
# ----------------------
def ices_init():
    print "ices_shuffle_playlist init"
    return 1    

def ices_shutdown():
    print "ices shutdown"
    return 1

def ices_get_next():
    return PlaylistManager.get_manager().get_random_track()

def ices_get_metadata():
    return PlaylistManager.get_manager().get_metadata()    
