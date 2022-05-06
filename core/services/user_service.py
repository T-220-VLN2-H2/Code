from django.shortcuts import redirect
from core.models import Profile, UserRatings
from django.db.models import Avg
from models.user import User


class UserService:
    def get_user_info(self, user_id):
        user = Profile.objects.filter(id=user_id)
        return user

    def set_user_info(self, user_id, first_name=None, last_name=None, bio=None):
        user = self.get_user_info(user_id)
        if not user:
            return "404: User not found."
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if bio:
            user.bio = bio

    def create_user(form):
        pass

    def get_user_rating(user_id):
        rating = (
            UserRatings.objects.all().filter(ratee_id=user_id).aggregate(Avg("rating"))
        )
        if not rating:
            rating = "Not rated."
        return rating
