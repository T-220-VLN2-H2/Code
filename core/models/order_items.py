from django.db import models

# from .item import Item
from .order import Order


class OrderItems(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    # TODO: add items to model
    # items: array<Item>

    def getTotal(self) -> models.DecimalField:
        pass

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """

        db_table = "core_order_items"
        app_label = "core"
