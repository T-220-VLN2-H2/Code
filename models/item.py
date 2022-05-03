from django.db import models
# TODO: import deliveryType


class Item(models.Models):
    id = models.BigAutoField()
    price = models.DecimalField()
    condition = models.ConditionType()
    category = models.Category()
    # TODO: add delivery options
    # delivery_Options = models.Array<DeliveryType>()

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "firesale_item"
        app_label = "firesale"
