from core.models import Notification
from django.core.exceptions import ObjectDoesNotExist


class NotificationService:
    def send_notification(self, user, title, message):
        notification = Notification(title=title, message=message, user_id=user)
        notification.save()

    def get_notifications(self, user, only_unread=False):
        # TODO: remove nesting
        try:
            if only_unread:
                notifications = Notification.objects.get(user_id=user, read=False)
            else:
                notifications = Notification.objects.get(user_id=user)
        except ObjectDoesNotExist:
            return []

        return notifications

    def mark_notification_read(self, notification):
        notification.read = True
        notification.save()
        # TODO set DB notification 'read' as true
