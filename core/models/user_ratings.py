from django.db import models
from .user import User
from .order import Order


class UserRatings(models.Model):
    # rater = models.ForeignKey(User, on_delete=models.CASCADE)
    # ratee = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=1, decimal_places=0)

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """

        db_table = "core_user_ratings"
        app_label = "core"
