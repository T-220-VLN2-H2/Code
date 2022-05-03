from django.db import models
from .catagory import Catagory


# TODO: add display text
DELIVERY_TYPE = (
    ("DELIVERY", "Home delivery"),
    ("PICKUP", "Self pickup"),
    ("HANDOFF", "???"),
    )

CONDITION_TYPE = (
    ("NEW", ""),
    ("USED", ""),
    ("USED_LIKE_NEW", ""),
    ("FOR_PARTS", "For parts: not working"),
    )


class Item(models.Models):
    id = models.BigAutoField(primary_key=True)
    price = models.DecimalField()
    condition = models.CharField(choices=CONDITION_TYPE)
    category = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    # TODO: add delivery options
    # delivery_Options = models.Array<DeliveryType>()

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "firesale_item"
        app_label = "firesale"
