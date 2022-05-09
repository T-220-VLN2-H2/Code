from django.shortcuts import redirect
from core.models import User, UserRatings
from django.db.models import Avg


class UserService:
    def get_user_info(self, user_id):
        # keep this as .get, id is unique we only expect to receive one result
        user = User.objects.get(id=user_id)
        return user

    def set_user_info(self, user, first_name=None, last_name=None, bio=None):
        pass
        # probably won't need this

    def create_user(self, form):
        pass

    def add_user_rating(self, form, user):
        pass

    def get_user_rating(self, user_id):
        rating = UserRatings.objects.filter(ratee_id=user_id).aggregate(Avg("rating"))
        if not rating:
            rating = "Not rated."
        return rating

    def get_user_ratings(self, user_id, count=12):
        ratings = UserRatings.objects.filter(ratee_id=user_id).order_by("-id")[:12]
        return ratings
