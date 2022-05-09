from django.db import models
from django.utils.translation import gettext_lazy as _
import core.models as core
from django.contrib.auth.models import User


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    buyer = models.ForeignKey(
        User, related_name="buyer_users", on_delete=models.CASCADE
    )
    seller = models.ForeignKey(
        User, related_name="seller_users", on_delete=models.CASCADE
    )
    order_items = models.ForeignKey("OrderItems", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.id

    def displayOrderSummary(self) -> None:
        # TODO: docstring
        # TODO: implement, Should this be __sum__?
        pass

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """

        db_table = "core_order"
        app_label = "core"
