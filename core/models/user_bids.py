from django.core.validators import MinValueValidator
from decimal import Decimal
from django.db import models
from .item import Item
from .user import User


# TODO: rename offer?
class UserBids(models.Model):
    BID_STATUS = (
        ("REJECTED", "Rejected"),
        ("ACCEPTED", "Accepted"),
        ("PENDING", "Pending"),
        ("COMPLETED", "Completed"),
    )
    # TODO: remove id suffix?
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal("0.01"))]
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    expires = models.DateTimeField(blank=True)
    status = models.CharField(
        choices=BID_STATUS, default=BID_STATUS[2][0], max_length=128
    )

    def __str__(self):
        return f"{self.item_id.id}"

    class Meta:
        """
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """

        db_table = "core_user_bids"
        app_label = "core"
