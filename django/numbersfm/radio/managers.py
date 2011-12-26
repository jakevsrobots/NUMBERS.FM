from django.db.models import Manager


class StationStatusUpdateManager(Manager):
    def current_status(self):
        if self.count() == 0:
            return None

        return self.order_by('-timestamp')[0]
