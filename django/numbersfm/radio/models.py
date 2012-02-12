from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import User
from undermythumb.fields import ImageWithThumbnailsField, ImageFallbackField
from undermythumb.renderers import CropRenderer
from numbersfm.utils.managers import ActiveManager
from managers import StationStatusUpdateManager


class Show(models.Model):
    is_active = models.BooleanField(default=True, help_text="If this box is not checked, the show will still appear, but it will be listed as 'inactive'.")
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    short_description = models.TextField(blank=True)
    full_description = models.TextField(blank=True)
    
    # images
    image = ImageWithThumbnailsField(max_length=255, blank=True, upload_to='shows/',
                                     thumbnails=(('detail_page_image', CropRenderer(960, 296)),
                                                 ('thumb_image', CropRenderer(240, 240))),
                                     help_text='This image should be at least 960 pixels wide.')
    detail_page_image = ImageFallbackField(fallback_path='image.thumbnails.detail_page_image',
                                           upload_to='shows/',
                                           help_text='Optional override for detail page image crop. 960x296')
    thumb_image = ImageFallbackField(fallback_path='image.thumbnails.thumb_image',
                                           upload_to='shows/',
                                           help_text='Optional override for thumbnail image crop. 240x240')

    objects = ActiveManager()

    class Meta:
        ordering = ('name',)
    
    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('radio-show-detail', (self.slug,))

class ShowArchive(models.Model):
    show = models.ForeignKey(Show, related_name='archives')
    title = models.CharField(max_length=255)
    mp3 = models.FilePathField(path='/opt/mp3', max_length=255, blank=True)
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('ordering',)
    
    def __unicode__(self):
        return self.title

    def get_mp3_url(self):
        return self.mp3.replace('/opt/mp3','/archives')
    
class StationStatusUpdate(models.Model):
    """
    A snapshot of the current station status:
    - Live/archives
    - What show is currently playing.
    - What song is currently playing.    
    - When did this change occur.
    """
    
    is_live = models.BooleanField()
    current_show = models.ForeignKey(Show, blank=True, null=True)
    current_song = models.CharField(max_length=255, blank=True)
    timestamp = models.DateTimeField(default=datetime.now)

    objects = StationStatusUpdateManager()
    
    class Meta:
        ordering = ('-timestamp',)
    
    def __unicode__(self):
        return "status update #%s" % self.pk

    def get_description(self):
        if self.is_live:
            return "%s -- %s" % (self.current_show.name, self.current_song)
        else:
            return "[Archive Stream] %s" % self.current_song
    
    def song_duration(self):
        if StationStatusUpdate.objects.current_status() == self:
            return datetime.now() - self.timestamp
        else:
            try:
                next_update = StationStatusUpdate.objects.exclude(current_song=self.current_song).filter(timestamp__gt=self.timestamp).order_by('timestamp')[0]
            except IndexError:
                return None
            return next_update.timestamp - self.timestamp

    def show_duration(self):
        if StationStatusUpdate.objects.current_status() == self:
            try:
                last_update = StationStatusUpdate.objects.exclude(current_show=self.current_show).filter(timestamp__lt=self.timestamp).order_by('-timestamp')[0]
            except IndexError:
                return None
            
            return datetime.now() - last_update.timestamp
        else:
            try:
                next_update = StationStatusUpdate.objects.exclude(current_show=self.current_show).filter(timestamp__gt=self.timestamp).order_by('timestamp')[0]
            except IndexError:
                return None
            
            return next_update.timestamp - self.timestamp
