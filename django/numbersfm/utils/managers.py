from datetime import datetime
from django.db import models


class ActiveManager(models.Manager):
    def active(self):
        return self.filter(is_active=True)

class PublishedManager(models.Manager):
    def published(self):
        return self.filter(is_published=True).filter(date_published__lte=datetime.now())
