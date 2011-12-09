from django.core.management import setup_environ
import settings
setup_environ(settings)
from radio.models import Show
from django.template.defaultfilters import slugify


artist_list = """
LORI FELKER
Camilla Ha
Sarah Weis
LAMPO
Shawn Decker
Julia Miller
ENEMY
Mark Booth
erica gressman
Entro MC
Lee Blalock
Brian Labycz
Cole Pierce
stasisfield
Alex Inglizian
Ryan T. Dunn
Nicholas Davis"""

def main():
    Show.objects.filter().delete()
    for artist in [x.strip() for x in artist_list.split("\n") if x.strip()]:
        Show.objects.get_or_create(name=artist, slug=slugify(artist), defaults={
                'schedule_type': 1
                })
    

if __name__ == '__main__':
    main()
