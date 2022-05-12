from django.shortcuts import redirect
from core.models import User, Order
from django.db.models import Avg


class UserService:
    @classmethod
    def get_user_info(cls, user_id):
        # keep this as .get, id is unique we only expect to receive one result
        user = User.objects.get(id=user_id)
        return user

    @classmethod
    def get_user_rating(cls, user_id):
        rating = Order.objects.filter(seller=user_id).aggregate(Avg("rating"))

        if not rating:
            rating = "Not rated."

        return rating

    @classmethod
    def get_user_ratings(cls, user_id, count=12):
        ratings = Order.objects.filter(seller=user_id, rating__isnull=False).order_by(
            "-id"
        )[:count]
        return ratings
