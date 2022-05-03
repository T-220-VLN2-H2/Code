from django.db import models


class UserRatings(models.Models):
    rater = models.User()
    ratee = models.User()
    order = models.Order()
    rating = models.DecimalField()

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "firesale_user_ratings"
        app_label = "firesale"
