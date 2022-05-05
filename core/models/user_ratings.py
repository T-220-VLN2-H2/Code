from django.db import models
from .user import User
from .order import Order
from django.utils.translation import gettext_lazy as _


class UserRatings(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=1, decimal_places=0)

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """

        db_table = "core_user_ratings"
        app_label = "core"


class RatingUsers(models.Model):
    class UserType(models.TextChoices):
        RATER = "Rater", _("")
        RATEE = "Ratee", _("")

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(choices=UserType.choices, max_length=128)
    user_rating = models.ForeignKey(UserRatings, on_delete=models.CASCADE)
