from datetime import datetime
from django.db import models
from radio.models import Show
from numbersfm.utils.managers import PublishedManager


class NewsPost(models.Model):
    is_published = models.BooleanField(default=False)
    date_published = models.DateTimeField(default=datetime.now)

    title = models.CharField(max_length=255)
    body = models.TextField(blank=True)

    related_shows = models.ManyToManyField(Show, blank=True)

    objects = PublishedManager()
    
    class Meta:
        ordering = ('-date_published',)
    
    def __unicode__(self):
        return self.title
