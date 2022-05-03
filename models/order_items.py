from django.db import models


class OrderItems(models.Models):
    order_id = models.BigIntergerField
    # TODO: add items to model
    # items: array<Item>

    def getTotal(self) -> models.DecimalField:
        pass

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "firesale_order_items"
        app_label = "firesale"
