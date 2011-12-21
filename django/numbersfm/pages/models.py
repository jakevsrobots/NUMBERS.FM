from django.db import models


class Page(models.Model):
    name = models.CharField(max_length=255, unique=True)
    body = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
    
    def __unicode__(self):
        return self.name
