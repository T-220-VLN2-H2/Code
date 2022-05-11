from core.services.notification_service import NotificationService


def notifications(request):
    return {
        "notifications": NotificationService.get_notifications(
            request.user, only_unread=True
        )
    }
