"""
A module used by `ices` to randomly play tracks from a folder.
"""

import os, random


# ----------------------
# Constants
# ----------------------
ARCHIVE_BASE_DIR = '/opt/mp3/'
NUM_RECENT_TRACKS_TO_COUNT = 10
RECENTLY_PLAYED_TRACKS = []


# ----------------------
# Utilities
# ----------------------
def record_played_track(track):
    RECENTLY_PLAYED_TRACKS.insert(track)
    RECENTLY_PLAYED_TRACKS = RECENTLY_PLAYED_TRACKS[NUM_RECENT_TRACKS_TO_COUNT:]
    
def get_random_track():
    music_files = [
        os.path.join(ARCHIVE_BASE_DIR, x) \
            for x in os.listdir(ARCHIVE_BASE_DIR) \
            if os.path.splitext(x)[1].lower() == 'mp3'
    ]

    counter = 0
    limit = len(music_files)
    while counter < limit:
        track = random.choice(music_files)
        if track not in RECENTLY_PLAYED_TRACKS:
            record_played_track(track)
            return track

    track = random.choice(music_files)
    record_played_track(track)
    return track

# ----------------------
# Ices hooks
# ----------------------
def ices_init():
    print "ices init"
    return 1    

def ices_shutdown():
    print "ices shutdown"
    return 1

def ices_get_next():
    return "/opt/mp3/numbersfm_intro.mp3"

def ices_get_metadata():
    return "You are listening to Numbers.FM"
