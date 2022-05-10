from core.models import Notification
from django.core.exceptions import ObjectDoesNotExist


class NotificationService:
    @classmethod
    def add_notification(cls, user, title, message):
        notification = Notification(title=title, message=message, user_id=user)
        notification.save()

    @classmethod
    def get_notifications(cls, user, only_unread=False):
        try:
            notifications = (
                Notification.objects.all().filter(user_id=user).order_by("-timestamp")
            )
            if only_unread:
                notifications = notifications.filter(read=False)
        except ObjectDoesNotExist:
            return []
        except TypeError:
            return []

        return notifications

    @classmethod
    def mark_notification_read(cls, notification):
        notification.read = True
        notification.save()
        # TODO set DB notification 'read' as true
