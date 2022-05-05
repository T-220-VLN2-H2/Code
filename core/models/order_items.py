from django.db import models
from .item import Item


class OrderItems(models.Model):
    order_id = models.ForeignKey("Order", on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)

    def __str__(self):
        return self

    def getTotal(self) -> models.DecimalField:
        pass

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """

        db_table = "core_order_items"
        app_label = "core"
