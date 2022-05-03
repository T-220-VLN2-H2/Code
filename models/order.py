from django.db import models


class Order(models.Models):
    id = models.BigAutoField()
    buyer = models.User()
    seller = models.User()
    order_items = models.OrderItems()

    def displayOrderSummary(self) -> None:
        # TODO: docstring
        # TODO: implement
        pass

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "firesale_order"
        app_label = "firesale"
