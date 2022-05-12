from core.services.notification_service import NotificationService
from core.services.user_service import UserService


def notifications(request):
    if request.user.is_authenticated:

        rating = UserService.get_user_rating(request.user)["rating__avg"]
        if rating is None:
            rating = "not rated"
    else:
        rating = None
    return {
        "notifications": NotificationService.get_notifications(
            request.user, only_unread=True
        ),
        "logged_in_user_rating": rating,
    }
