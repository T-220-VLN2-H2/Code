from core.services.notification_service import NotificationService


def notifications(request):
    notify_service = NotificationService()
    return {
        "notifications": notify_service.get_notifications(request.user, only_unread=True)
    }
