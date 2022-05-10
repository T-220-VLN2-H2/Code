from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .user import User
from .order import Order
from django.utils.translation import gettext_lazy as _


class UserRatings(models.Model):
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    rater = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="rater_users"
    )
    ratee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="ratee_users"
    )
    rating = models.SmallIntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return self

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """

        db_table = "core_user_ratings"
        app_label = "core"
