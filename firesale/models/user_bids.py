from django.db import models


class UserBids(models.Models):
    user_id = models.BigIntergerField()
    item_id = models.BigIntergerField()
    amount = models.BigIntergerField()
    timestamp = models.DateTimeField()
    expires = models.DateTimeField()

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "firesale_user_bids"
        app_label = "firesale"
