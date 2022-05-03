from django.db import models
from .item import Item
from .user import User


class UserBids(models.Models):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.DecimalField()
    timestamp = models.DateTimeField(auto_add_now=True)
    expires = models.DateTimeField()

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "firesale_user_bids"
        app_label = "firesale"
