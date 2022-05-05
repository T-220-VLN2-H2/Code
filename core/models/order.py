from django.db import models
from django.utils.translation import gettext_lazy as _
from .user import User


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    users = models.ManyToManyField(User, through="OrderUser")
    order_items = models.ForeignKey("OrderItems", on_delete=models.CASCADE)

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


class OrderUser(models.Model):
    class UserType(models.TextChoices):
        BUYER = "Buyer", _("")
        SELLER = "Seller", _("")

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(choices=UserType.choices, max_length=128)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
