from django.db import models
from django.contrib.auth.models import User
from undermythumb.fields import ImageWithThumbnailsField, ImageFallbackField
from undermythumb.renderers import CropRenderer


SHOW_SCHEDULE_TYPES = (
    (0, 'Single'),
    (1, 'Recurring')
)

class Show(models.Model):
    users = models.ManyToManyField(User, help_text='Users who may edit info about this show.')
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    schedule_type = models.PositiveIntegerField(choices=SHOW_SCHEDULE_TYPES)
    short_description = models.TextField(blank=True)
    full_description = models.TextField(blank=True)
    
    # images
    image = ImageWithThumbnailsField(max_length=255, upload_to='shows/',
                                     thumbnails=(('detail_page_image', CropRenderer(960, 196)),
                                                 ('thumb_image', CropRenderer(240, 240))),
                                     help_text='This image should be at least 960 pixels wide.')
    detail_page_image = ImageFallbackField(fallback_path='image.thumbnails.detail_page_image',
                                           upload_to='shows/',
                                           help_text='Optional override for detail page image crop. 960x196')
    thumb_image = ImageFallbackField(fallback_path='image.thumbnails.thumb_image',
                                           upload_to='shows/',
                                           help_text='Optional override for thumbnail image crop. 240x240')

    def __unicode__(self):
        return self.name
