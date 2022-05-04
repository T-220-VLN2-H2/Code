from django.db import models
from django.utils.translation import gettext_lazy as _

# from .order_items import OrderItems
from .user import User


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
<<<<<<< HEAD
    # buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    # seller = models.ForeignKey(User, on_delete=models.CASCADE)
=======
    users = models.ManyToManyField(User, through="OrderUser")
>>>>>>> origin/main
    # order_items = models.ForeignKey(OrderItems, on_delete=models.CASCADE)

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


class OrderUser(models.Model):
    class UserType(models.TextChoices):
        BUYER = "Buyer", _("")
        SELLER = "Seller", _("")

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(choices=UserType.choices, max_length=128)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
