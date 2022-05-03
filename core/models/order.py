from django.db import models
from .order_items import OrderItems
from .user import User


class Order(models.Models):
    id = models.BigAutoField(primary_key=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    order_items = models.ForeignKey(OrderItems, on_delete=models.CASCADE)

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
