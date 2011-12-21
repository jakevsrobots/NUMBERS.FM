from django.db import models
from django.contrib.auth.models import User
from undermythumb.fields import ImageWithThumbnailsField, ImageFallbackField
from undermythumb.renderers import CropRenderer
from numbersfm.utils.managers import ActiveManager


class Show(models.Model):
    is_active = models.BooleanField(default=True, help_text="If this box is not checked, the show will not appear on the site.")
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    short_description = models.TextField(blank=True)
    full_description = models.TextField(blank=True)
    
    # images
    image = ImageWithThumbnailsField(max_length=255, upload_to='shows/',
                                     thumbnails=(('detail_page_image', CropRenderer(960, 300)),
                                                 ('thumb_image', CropRenderer(240, 240))),
                                     help_text='This image should be at least 960 pixels wide.')
    detail_page_image = ImageFallbackField(fallback_path='image.thumbnails.detail_page_image',
                                           upload_to='shows/',
                                           help_text='Optional override for detail page image crop. 960x196')
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
