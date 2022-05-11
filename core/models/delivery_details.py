from django.db import models

from core.models.user_bids import UserBids


class DeliveryMethod(models.Model):
    DEL_METHOD = (
        ("Delivery service", "Delivery service"),
        ("Pick up", "Pick up"),
        ("Postbox", "Postbox"),
        ("Speak with seller", "Speak with seller"),
    )
    bid_id =  models.ForeignKey(UserBids, on_delete=models.CASCADE)
    del_choice = models.CharField(choices=DEL_METHOD, max_length=128)

    def __str__(self):
        return "User delivery choice for order"

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """

        db_table = "core_delivery_method"
        app_label = "core"
