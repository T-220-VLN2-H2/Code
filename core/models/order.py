from django.db import models
# from .order_items import OrderItems
from .user import User


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="buyer_users")
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seller_users")
    #order_items = models.ForeignKey(OrderItems, on_delete=models.CASCADE)

    def displayOrderSummary(self) -> None:
        # TODO: docstring
        # TODO: implement
        pass

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "core_order"
        app_label = "core"
