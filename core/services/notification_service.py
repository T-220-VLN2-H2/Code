from core.models import Notification
from django.core.exceptions import ObjectDoesNotExist


class NotificationService:
    def add_notification(self, user, title, message):
        notification = Notification(title=title, message=message, user_id=user)
        notification.save()

    @staticmethod
    def get_notifications(user, only_unread=False):
        try:
            notifications = Notification.objects.all().filter(user_id=user)
            if only_unread:
                notifications = notifications.filter(read=False)
        except ObjectDoesNotExist:
            return []

        return notifications

    def mark_notification_read(self, notification):
        notification.read = True
        notification.save()
        # TODO set DB notification 'read' as true
