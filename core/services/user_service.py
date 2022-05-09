from django.shortcuts import redirect
from core.models import User, UserRatings
from django.db.models import Avg


class UserService:
    def get_user_info(self, user_id):
<<<<<<< HEAD
        user = User.objects.filter(id=user_id)
=======
        user = Profile.objects.get(id=user_id)
>>>>>>> origin/main
        return user

    def set_user_info(self, user, first_name=None, last_name=None, bio=None):
        pass
        # probably won't need this

    def create_user(form):
        pass

    def get_user_rating(user_id):
        rating = (
            UserRatings.objects.all().filter(ratee_id=user_id).aggregate(Avg("rating"))
        )
        if not rating:
            rating = "Not rated."
        return rating
